from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from server.app.config import Config




db = SQLAlchemy()

from server.app.models import User, Friendship, UserAttr

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Настройка конфигурации
    app.config.from_object(config_class)

    # Инициализация базы данных
    db.init_app(app)

    app.app_context().push()

    with app.app_context():
        db.session.execute(text("CREATE SCHEMA IF NOT EXISTS app"))
        db.session.commit()
        db.create_all()
    
    # Регистрация Blueprint
    from server.app.routes import bp
    app.register_blueprint(bp)

    return app, db

# Создаем приложение
# app, db = create_app()
