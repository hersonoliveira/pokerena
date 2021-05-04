from datetime import datetime

from pokerena import db


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
    email = db.Column(db.String, nullable=False)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


# class Club(db.Model):
#     pass


# class GamesFact(db.Model):
#     pass
