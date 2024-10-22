import json

from flask import Blueprint
from flask import Flask, render_template, session, request, jsonify, current_app  # глобальный объект приложения импортируем
from psycopg2 import OperationalError


from app.models import User, UserAttr, Friendship
from app.create_app import db

bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the app!'
    }), 200


# {
#   "username": "john_doe",
#   "email": "john@example.com",
#   "password": "secure_password123",
#   "country": "USA",
#   "city": "New York"
# }
# Создание пользователя и его профиля
@bp.route("/users", methods=['POST'])
def create_user():
    data = request.json
    
    # Проверка обязательных полей
    required_fields = ['username', 'email', 'password', 'country', 'city']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            'error': 'Отсутствуют обязательные поля',
            'fields': missing_fields
        }), 400

    # Создание нового пользователя
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],  # Предполагается, что у вас есть функция hash_password
        country=data['country'],
        city=data['city']
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'message': 'Пользователь успешно создан!',
            'user_id': new_user.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
