from flask import Blueprint


games_blueprint = Blueprint("games", __name__, template_folder="templates")

from . import routes
