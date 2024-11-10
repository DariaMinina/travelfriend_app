from server.app.create_app import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        "schema":"app"
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))


class UserAttr(db.Model):
    __tablename__ = 'user_attr'
    __table_args__ = {
        "schema":"app"
    }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer,
        nullable=False)
    interest = db.Column(db.String(128), nullable=False)


class Friendship(db.Model):
    __tablename__ = 'friendship'
    __table_args__ = {
        "schema":"app"
    }
    user_id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    friend_id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
