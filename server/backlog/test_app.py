import pytest
from flask import json
from run import app, db
from app import create_app
from app.models import User, Friendship


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as c:
        yield c


def test_search_friends_user(client):
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
    data_user3 = {
        'username': 'User3',
        'email': 'User3@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    user1 = User(**data_user1)
    user2 = User(**data_user2)
    user3 = User(**data_user3)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    friendship1 = Friendship(user_id=user1.id, friend_id=user2.id)
    friendship2 = Friendship(user_id=user1.id, friend_id=user3.id)
    db.session.add(friendship1)
    db.session.add(friendship2)
    db.session.commit()

    # Проверяем поиск дружеских пользователей
    response = client.get('/friends/1?limit=5&offset=0')
    assert response.status_code == 200
    assert len(response.json['data']) == 2
    assert response.json['data'][0]['username'] == 'User2'
    assert response.json['data'][1]['username'] == 'User3'

    # Проверяем отсутствие пользователя
    response = client.get('/friends/999?limit=5&offset=0')
    assert response.status_code == 404
    assert response.json['error'] == 'User not found'

    # Очищаем тестовые данные
    db.session.query(User).delete()
    db.session.query(Friendship).delete()
    db.session.commit()

def test_search_friends_limit_offset(client):
    # Создаем тестовых пользователей и дружбы
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
    data_user3 = {
        'username': 'User3',
        'email': 'User3@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    data_user4 = {
        'username': 'User3',
        'email': 'User3@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    user1 = User(**data_user1)
    user2 = User(**data_user2)
    user3 = User(**data_user3)
    user4 = User(**data_user4)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.commit()

    friendship1 = Friendship(user_id=user1.id, friend_id=user2.id)
    friendship2 = Friendship(user_id=user1.id, friend_id=user3.id)
    friendship3 = Friendship(user_id=user1.id, friend_id=user4.id)
    db.session.add(friendship1)
    db.session.add(friendship2)
    db.session.add(friendship3)
    db.session.commit()

    # Проверяем ограничение лимита
    response = client.get('/friends/1?limit=2&offset=0')
    assert response.status_code == 200
    assert len(response.json['data']) == 2

    # Проверяем выравнивание результатов
    response = client.get('/friends/1?limit=2&offset=1')
    assert response.status_code == 200
    assert len(response.json['data']) == 1

    # Очищаем тестовые данные
    db.session.query(User).delete()
    db.session.query(Friendship).delete()
    db.session.commit()

def test_empty_results(client):
    # Создаем пользователя без дружб
    data_user = {
        'username': 'User',
        'email': 'User@example.com',
        'password': 'testpass123',
        'country': 'Russia',
        'city': 'Moscow'
    }
    user = User(**data_user)
    db.session.add(user)
    db.session.commit()

    response = client.get('/friends/1?limit=5&offset=0')
    assert response.status_code == 200
    assert len(response.json['data']) == 0

    # Очищаем тестовые данные
    db.session.delete(user)
    db.session.commit()