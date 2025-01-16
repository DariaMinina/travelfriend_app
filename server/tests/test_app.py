import pytest
from flask import json
from sqlalchemy import text

from server.run import app
from server.run import db 
from server.app import create_app
from server.app.models import User, Friendship


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as c:
        yield c


def test_create_user(client):
    with client.application.app_context():
        db.session.execute(text("CREATE SCHEMA IF NOT EXISTS app"))
        db.session.commit()
        db.create_all()
    data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'country': 'Russia',
            'city': 'Moscow'
    }

    # Отправка запроса на создание нового пользователя
    response = client.post('/users', json=data)

    # Проверяем результат
    assert response.status_code == 201
    assert 'message' in response.json
    assert 'user_id' in response.json

    with client.application.app_context():
        db.session.query(User).filter_by(username='testuser').delete()
        db.session.commit()


def test_missing_required_field(client):
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123',
        'country': 'Russia'
    }
    response = client.post('/users', json=data)
    assert response.status_code == 400
    assert 'error' in response.json
    assert 'fields' in response.json


def test_database_error(client):
    # Начало транзакции
    with db.session.begin_nested():
        data = {
            'username': 'existing_user',
            'email': 'existing_user@example.com',
            'password': 'testpass123',
            'country': 'Russia',
            'city': 'Moscow'
        }
        
        # Попытка добавить существующего пользователя
        db.session.add(User(**data))
        
        # Отправка запроса на создание нового пользователя
        response = client.post('/users', json=data)
        
        # Проверки
        assert response.status_code == 500
        assert 'error' in response.json
        
        # Очистка базы данных после теста
        db.session.rollback()


def test_add_friendship(client):
    # Создаем тестовых пользователей
    data_user1 = {
        'username': 'User1',
        'email': 'User1@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    data_user2 = {
        'username': 'User2',
        'email': 'User2@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    user1 = User(**data_user1)
    user2 = User(**data_user2)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()


    # Отправляем запрос на добавление дружбы
    data = {'user_id': user1.id, 'friend_id': user2.id}
    response = client.post('/friendships', json=data)

    assert response.status_code == 201
    assert response.json['message'] == 'Запрос на дружбу создан'

    # Проверяем, что дружба была создана
    friendship = Friendship.query.filter((Friendship.user_id == user1.id) & 
                                        (Friendship.friend_id == user2.id)).first()
    assert friendship is not None

    # Очищаем тестовые данные
    db.session.delete(user1)
    db.session.delete(user2)
    db.session.commit()

def test_add_friendship_invalid_data(client):
    response = client.post('/friendships', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Отсутствуют user_id или friend_id'

    response = client.post('/friendships', json={'invalid': 'data'})
    assert response.status_code == 400
    assert response.json['error'] == 'Отсутствуют user_id или friend_id'

def test_add_friendship_nonexistent_user(client):
    response = client.post('/friendships', json={'user_id': 999, 'friend_id': 1000})
    assert response.status_code == 404
    assert response.json['error'] == 'Один или оба пользователя отсутствуют'


def test_add_friendship_with_errors(client):
    # Создаем тестовых пользователей
    data_user1 = {
        'username': 'User1',
        'email': 'User1@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    user1 = User(**data_user1)
    db.session.add(user1)
    db.session.commit()

    # Попытка добавить дружбу без friend_id
    response = client.post('/friendships', json={'user_id': user1.id})
    assert response.status_code == 400
    assert response.json['error'] == 'Отсутствуют user_id или friend_id'

    # Очищаем тестовые данные
    db.session.delete(user1)
    db.session.commit()

