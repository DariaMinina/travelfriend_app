import json

from flask import Flask, render_template, session, request, jsonify, current_app  # глобальный объект приложения импортируем
from psycopg2 import OperationalError

from database import PostgreSQLHandler

app = Flask(__name__)  # __name__ имя модуля, точка входа

app.config['SECRET_KEY'] = 'I am the only one'

app.config['DB_CONFIG'] = {
    'host': 'localhost',
    'port': 5432,
    'user': 'root',
    'password': 'root',
    'database': 'travel_app'
}


# {
#   "username": "john_doe",
#   "email": "john@example.com",
#   "password": "secure_password123",
#   "country": "USA",
#   "city": "New York"
# }
# Создание пользователя и его профиля
@app.route("/users", methods=['POST'])
def create_user():

    handler = PostgreSQLHandler(
        current_app.config['DB_CONFIG']
    )

    # Подключение к базе данных
    if not handler.connect():
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    # Получаем данные из запроса
    data = request.json

    # Проверяем наличие обязательных полей
    required_fields = ['username', 'email', 'password', 'country', 'city']
    missing_fields = [field for field in required_fields if field not in data]
        
    if missing_fields:
        return jsonify({
            'error': 'Missing required fields',
            'fields': missing_fields
        }), 400

    # Если все поля есть, продолжаем обработку
    dict_fields = {req_field : data[req_field] for req_field in required_fields}
    
    # Загрузка данных в базу
    if handler.load_data("app.users", data):
        result = handler.execute_query("SELECT * FROM app.users WHERE email = %s", (data['email'],))
        
        return jsonify({
            'message': 'Данные успешно получены!',
            'result': result
        }), 200
    else:
        return jsonify({'error': 'Failed to load data'}), 500


    if hasattr(handler, 'connection'):
        handler.close_connection()

    return jsonify({
        'message': 'Данные успешно получены',
        'data': dict_fields
    }), 200


# Параметры: ?country=France&interests=cycling,hiking
# Эта операция позволит искать потенциальных друзей на основе различных критериев.
@app.route("/friends/search", methods=['GET'])
def search_friends():

    handler = PostgreSQLHandler(
        current_app.config['DB_CONFIG']
    )

    # Подключение к базе данных
    if not handler.connect():
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    # Получаем параметры запроса
    country = request.args.get('country', None)
    interests = request.args.get('interests', None)

    if interests is not None:
        interests_str = repr(tuple(interests.split(',')))
        interests_conditions = rf"AND interest IN {interests_str}"

    if country is not None:
        country_str = f"'{country}'"
        country_conditions = rf"AND country = {country_str}"

    # Формируем запрос
    query = f"""
        SELECT u.username, u.city, STRING_AGG(ua.interest, ', ') as interests
        FROM app.users u 
            INNER JOIN app.user_attr ua 
            ON u.id = ua.user_id 
        WHERE 1 = 1 
        {interests_conditions}
        {country_conditions}
        GROUP BY u.username, u.city 
    """

    print(query)

    try:
        result = handler.execute_query(query=query)
    except OperationalError as err:
        return jsonify({
            'error': 'Проблемы с поиском друзей в базе'
        }), 500

    if hasattr(handler, 'connection'):
        handler.close_connection()

    return jsonify({
        'message': 'Данные успешно получены',
        'data': result
    }), 200



if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5015)
