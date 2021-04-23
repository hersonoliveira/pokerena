from . import games_blueprint
from flask import render_template, request, session, redirect, url_for


@games_blueprint.route("/")
def index():
    return render_template("games/index.html")


@games_blueprint.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        for key, value in request.form.items():
            print(f"key: {key} | value: {value}")

        # Save form data to the session object
        session["game_name"] = request.form["game_name"]
        session["date"] = request.form["date"]
        session["players"] = request.form["players"]
        return redirect(url_for("games.list_games"))

    return render_template("games/add_game.html")


@games_blueprint.route("/list_games")
def list_games():
    return render_template("games/games.html")
