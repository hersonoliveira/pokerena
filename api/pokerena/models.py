from datetime import datetime

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
    game_facts = db.relationship("GamesFact", backref="game", lazy="dynamic")

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
    email = db.Column(db.String, nullable=False, unique=True)
    password_hashed = db.Column(db.String)
    game_facts = db.relationship("GamesFact", backref="user", lazy="dynamic")

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


class GamesFact(db.Model):
    """
    Fact table for games results
    """

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    rebuy = db.Column(db.Integer, nullable=False)
    add_on = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<GamesFact(game_id={self.game_id}, user_id={self.user_id}, position={self.position}, rebuy={self.rebuy}, add_on={self.add_on})>"
