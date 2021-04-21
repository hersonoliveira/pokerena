from . import games_blueprint
from flask import render_template


@games_blueprint.route("/")
def index():
    return render_template("games/index.html")
