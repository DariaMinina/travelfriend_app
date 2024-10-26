import sys
import os

# Добавляем корневую директорию проекта в PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app.create_app import create_app
from server.app.config import Config


app, db = create_app()

if __name__ == '__main__':
    app.run(debug=True)