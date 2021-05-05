from pokerena import create_app, db
import pytest
from flask import current_app


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.from_object("config.TestingConfig")

    with app.test_client() as testing_client:
        with app.app_context():
            current_app.logger.info("In the test_client() fixture, creating db...")

            db.create_all()
    
    yield testing_client

    with app.app_context():
        db.drop_all()
