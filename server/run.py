from server.app.create_app import create_app
from server.app.config import Config

app, db = create_app()

if __name__ == '__main__':
    app.run(debug=True)