from pokerena import db


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()


class User(db.Model):
    pass


class Club(db.Model):
    pass


class GamesFact(db.Model):
    pass
