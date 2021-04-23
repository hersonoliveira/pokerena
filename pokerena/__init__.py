import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = b"\x91\xd7\x15\x96\xb9=\x8c\x03\xfe\xc0vX\xe9\x14h[\x95\xa8\xaf\xcf>\x1a\x0e\xfb\x0e3\x97/P\x9e\xef9"

    # Configure the Flask app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # Logging config
    _config_logging(app)
    app.logger.info("Starting the Pokerena App")

    # Register blueprints
    _register_blueprints(app)

    return app


def _register_blueprints(app):
    from pokerena.games import games_blueprint
    from pokerena.users import users_blueprint

    app.register_blueprint(games_blueprint)
    app.register_blueprint(users_blueprint)


def _config_logging(app):
    file_handler = RotatingFileHandler(
        filename="instance/pokerena.log",
        maxBytes=16000,
        backupCount=10,
    )
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)
