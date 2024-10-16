import json

from flask import Flask, render_template, session, request, jsonify  # глобальный объект приложения импортируем


app = Flask(__name__)  # __name__ имя модуля, точка входа

app.config['SECRET_KEY'] = 'I am the only one'

app.config['DB_CONFIG'] = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'travel_app'
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

    return jsonify({
        'message': 'Данные успешно получены',
        'data': dict_fields
    }), 200


if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5015)
