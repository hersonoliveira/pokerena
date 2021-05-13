import pytest
from flask import current_app
from pokerena import create_app, db
from pokerena.models import User


@pytest.fixture(scope="module")
def test_client():
    app = _get_flask_test_app()

    with app.test_client() as testing_client:
        with app.app_context():
            current_app.logger.info("In the test_client() fixture, creating db...")
            db.create_all()

            yield testing_client

            db.drop_all()


@pytest.fixture(scope="module")
def new_user():
    app = _get_flask_test_app()

    with app.app_context():
        user = User("dummy_user", "dummy@me.com", "1234")
        yield user


def _get_flask_test_app():
    app = create_app()
    app.config.from_object("config.TestingConfig")
    return app
