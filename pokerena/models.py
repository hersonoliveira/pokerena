from datetime import datetime
from enum import unique

from flask import current_app

from pokerena import db, bcrypt


class Game(db.Model):
    """
    Representation of a poker game
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, name: str, description: str, date: datetime):
        self.name = name
        self.description = description
        self.date = date

    def __repr__(self):
        return f"<Game(name='{self.name}', description='{self.description}', date='{self.date}')>"


class User(db.Model):
    """
    Representation of a user/poker player
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password_hashed = db.Column(db.String)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password_hashed = bcrypt.generate_password_hash(
            password,
            current_app.config.get("BCRYPT_LOG_ROUNDS"),
        ).decode("utf-8")

    def is_password_correct(self, password: str):
        return bcrypt.check_password_hash(self.password_hashed, password)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


# class Club(db.Model):
#     pass


# class GamesFact(db.Model):
#     pass
