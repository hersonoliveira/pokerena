import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_migration = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.secret_key = b"\x91\xd7\x15\x96\xb9=\x8c\x03\xfe\xc0vX\xe9\x14h[\x95\xa8\xaf\xcf>\x1a\x0e\xfb\x0e3\x97/P\x9e\xef9"

    # Configure the Flask app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # Logging config
    _config_logging(app)
    app.logger.info("Starting the Pokerena App")

    # Initialize extensions
    init_extensions(app)

    # Register blueprints
    _register_blueprints(app)

    # Register error pages
    _register_error_pages(app)

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
    file_formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]"
    )
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)


def _register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404


def init_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    bcrypt.init_app(app)
