import pytest
from flask import json
from your_app import create_app, db
from your_app.routes import user_routes
from your_app.models.user import User

@pytest.fixture
def app():
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(app, client):
    # Подготовка тестовых данных
    test_user = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123',
        'country': 'Test Country',
        'city': 'Test City'
    }

    # Отправка POST-запроса
    response = client.post('/users', json=test_user)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка содержимого ответа
    data = response.json
    assert 'message' in data
    assert 'result' in data

    # Проверка сохранения пользователя в базе данных
    db_user = User.query.filter_by(email=test_user['email']).first()
    assert db_user is not None
    assert db_user.username == test_user['username']
    assert db_user.email == test_user['email']

def test_create_user_missing_fields(app, client):
    # Отправка POST-запроса без обязательных полей
    response = client.post('/users', json={})

    # Проверка статуса ответа и содержимого
    assert response.status_code == 400
    data = response.json
    assert 'error' in data
    assert 'fields' in data
    missing_fields = ['username', 'email', 'password', 'country', 'city']
    assert set(data['fields']) == set(missing_fields)

def test_create_user_invalid_email(app, client):
    invalid_emails = [
        'invalid.email',
        '@example.com',
        'example@'
    ]
    
    for email in invalid_emails:
        test_user = {
            'username': 'testuser',
            'email': email,
            'password': 'testpass123',
            'country': 'Test Country',
            'city': 'Test City'
        }
        
        response = client.post('/users', json=test_user)
        
        assert response.status_code == 400
        data = response.json
        assert 'error' in data

def test_create_user_database_error(app, client):
    # Мокирование функции load_data для имитации ошибки базы данных
    with mock.patch('your_app.routes.PostgreSQLHandler.load_data') as mock_load_data:
        mock_load_data.return_value = False
        
        response = client.post('/users', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'country': 'Test Country',
            'city': 'Test City'
        })
        
        assert response.status_code == 500
        data = response.json
        assert 'error' in data
