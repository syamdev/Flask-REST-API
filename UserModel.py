from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    # commands to create model in console
    # from UserModel import *
    # db.create_all()
    # cat database.db

    def __repr__(self):
        return str({
            'username': self.username,
            'password': self.password
        })

    def username_password_match(_username, _password):
        user = User.query.filter_by(username=_username).filter_by(password=_password).first()
        if user is None:
            return False
        else:
            return True

    def get_all_users():
        return User.query.all()

    def create_user(_username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()

    # commands to create user, etc
    # User.create_user('user1', 'password')
    # User.get_all_users()
    # User.username_password_match('user1', 'password')
