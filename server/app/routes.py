import json


from sqlalchemy import text
from flask import Blueprint
from flask import Flask, render_template, session, request, jsonify, current_app  # глобальный объект приложения импортируем
from psycopg2 import OperationalError


from server.app.models import User, UserAttr, Friendship
from server.app.create_app import db

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
    

# Параметры: ?country=France&interests=cycling,hiking
# Эта операция позволит искать потенциальных друзей на основе различных критериев.
@bp.route("/friends/search", methods=['GET'])
def search_friends():

    interests = request.args.get('interests')
    country = request.args.get('country')
    
    if not interests or not country:
        return jsonify({"error": "Both interest and country parameters are required"}), 400
    
    if interests is not None:
        interests_str = repr(tuple(interests.split(',')))
        interests_conditions = rf"AND interest IN {interests_str}"

    if country is not None:
        country_str = f"'{country}'"
        country_conditions = rf"AND country = {country_str}"

    # Формируем запрос
    query = f"""
        SELECT u.id, u.username, u.city, STRING_AGG(ua.interest, ', ') as interests
        FROM app.users u 
            INNER JOIN app.user_attr ua 
            ON u.id = ua.user_id 
        WHERE 1 = 1 
        {interests_conditions}
        {country_conditions}
        GROUP BY u.id, u.username, u.city 
    """
    
    sql = text(query)    

    try:
        result = db.session.execute(sql)
        columns = list(result.keys())
        results = [dict(zip(columns, row)) for row in result.fetchall()]
    except OperationalError as err:
        return jsonify({
            'error': 'Проблемы с поиском друзей в базе'
        }), 500
    

    return jsonify({
        'message': 'Данные успешно получены',
        'data': results
    }), 200


# {
#   "user_id": 123,
#   "friend_id": 456
# }
# Запрос на дружбу
@bp.route('/friendships', methods=['POST'])
def add_friendship():
    data = request.json
    
    if not data or 'user_id' not in data or 'friend_id' not in data:
        return jsonify({"error": "Отсутствуют user_id или friend_id"}), 400
    
    user_id = data['user_id']
    friend_id = data['friend_id']
    
    # Проверяем существование пользователей
    if not User.query.filter(User.id == user_id).first() or not User.query.filter(User.id == friend_id).first():
        return jsonify({"error": "Один или оба пользователя отсутствуют"}), 404
    
    # Создаем новую запись Friendship
    friendship = Friendship(user_id=user_id, friend_id=friend_id)
    db.session.add(friendship)
    friendship = Friendship(user_id=friend_id, friend_id=user_id)
    db.session.add(friendship)
    
    try:
        db.session.commit()
        return jsonify({"message": "Запрос на дружбу создан"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Параметры: ?limit=20&offset=0
# Эта операция позволит отображать текущий список друзей пользователя.
@bp.route("/friends/<int:userId>", methods=['GET'])
def search_friends_user(userId):
    # Проверяем существование пользователя
    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    limit = int(request.args.get('limit', 20))
    offset = int(request.args.get('offset', 0))

    # Получаем всех дружеских пользователей текущего пользователя
    friendships = Friendship.query.filter(Friendship.user_id == userId).all()

    # Собираем список дружеских пользователей
    friends = [
        {
            'user_id': User.query.get(friend_id).id,
            'username': User.query.get(friend_id).username,
            'email': User.query.get(friend_id).email,
            'country': User.query.get(friend_id).country,
            'city': User.query.get(friend_id).city
        } for friend_id in [friendship.friend_id for friendship in friendships]
    ]

    # Ограничиваем и выравниваем результаты
    friends = friends[offset:offset+limit]

    return jsonify({
        'message': 'Данные успешно получены',
        'data': friends
    }), 200



# {
#   "country": "Canada",
#   "city": "Toronto"
# }
@bp.route("/users/<int:userId>", methods=['PATCH'])
def update_user_info(userId):
    data = request.json
    if not userId:
        return jsonify({"error": "user_id является обязательным атрибутом"}), 400

    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "Пользователь не найден"}), 404

    # Обновляем только те поля, которые были переданы в запросе
    for key, value in data.items():
        if hasattr(user, key) and key != 'id':
            setattr(user, key, value)

    try:
        db.session.commit()
        return jsonify({"message": "Пользователь успешно обновлен"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

@bp.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "Пользователь не найден"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Пользователь успешно удален"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
