from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = b"\x91\xd7\x15\x96\xb9=\x8c\x03\xfe\xc0vX\xe9\x14h[\x95\xa8\xaf\xcf>\x1a\x0e\xfb\x0e3\x97/P\x9e\xef9"

    # Configure the Flask app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # Register blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    from pokerena.games import games_blueprint

    app.register_blueprint(games_blueprint)
