from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from server.app.config import Config




db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Настройка конфигурации
    app.config.from_object(config_class)

    # Инициализация базы данных
    db.init_app(app)

    app.app_context().push()

    with app.app_context():
        db.create_all()
    
    # Регистрация Blueprint
    from server.app.routes import bp
    app.register_blueprint(bp)

    return app, db

# Создаем приложение
# app, db = create_app()