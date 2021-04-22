from flask import render_template, request, session, url_for, redirect
from pokerena import create_app


app = create_app()


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        for key, value in request.form.items():
            print(f"key: {key} | value: {value}")

        # Save form data to the session object
        session["game_name"] = request.form["game_name"]
        session["date"] = request.form["date"]
        session["players"] = request.form["players"]
        return redirect(url_for("list_games"))

    return render_template("add_game.html")


@app.route("/list_games")
def list_games():
    return render_template("games.html")
