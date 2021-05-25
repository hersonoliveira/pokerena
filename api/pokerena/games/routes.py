from datetime import datetime

from flask import current_app, redirect, render_template, request, url_for
from pokerena import db
from pokerena.models import Game

from . import games_blueprint


@games_blueprint.route("/")
def index():
    return render_template("games/index.html")


@games_blueprint.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        new_game = Game(
            name=request.form["game_name"],
            description=request.form["description"],
            date=datetime.fromisoformat(request.form["date"]),
        )
        print(request.form["date"])
        # Commit to datadase
        db.session.add(new_game)
        db.session.commit()
        current_app.logger.info(f"New game added: {new_game}")

        return redirect(url_for("games.list_games"))

    return render_template("games/add_game.html")


@games_blueprint.route("/list_games")
def list_games():
    games = Game.query.order_by(Game.id).all()
    return render_template("games/games.html", games=games)
