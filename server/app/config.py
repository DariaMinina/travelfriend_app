import os
from dotenv import load_dotenv

# Загрузка переменных окружения
basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))
load_dotenv()

class Config:
    # Общие настройки
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = bool(os.getenv('DEBUG', False))
    TESTING = bool(os.getenv('TESTING', False))

    # Настройки базы данных
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Другие настройки
    SERVER_NAME = os.getenv('SERVER_NAME')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
