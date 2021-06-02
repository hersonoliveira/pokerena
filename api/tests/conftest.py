import pytest
from flask import current_app
from pokerena import create_app, db
from pokerena.models import Game, User
from datetime import datetime


@pytest.fixture(scope="function")
def test_client():
    app = _get_flask_test_app()

    with app.test_client() as testing_client:
        with app.app_context():
            current_app.logger.info("In the test_client() fixture, creating db...")
            db.drop_all()
            db.create_all()

            yield testing_client


@pytest.fixture(scope="module")
def new_user():
    app = _get_flask_test_app()

    with app.app_context():
        user = User("dummy_user", "dummy@me.com", "1234")
        yield user


@pytest.fixture(scope="function")
def populate_db(test_client):
    game = Game("pokerena", "Dummy game", datetime.fromisoformat("2021-05-27"))
    db.session.add(game)
    db.session.commit()

    yield test_client


def _get_flask_test_app():
    app = create_app()
    app.config.from_object("config.TestingConfig")
    return app
