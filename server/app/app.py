from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Настройка конфигурации
    app.config.from_object(config_class)
    
    # Инициализация базы данных
    db.init_app(app)
    
    return app, db

# Создаем приложение
app, db = create_app()