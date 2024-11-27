import sys
import os

# Добавляем корневую директорию проекта в PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app.create_app import create_app
from server.app.config import Config
from flask_cors import CORS


app, db = create_app()

CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
