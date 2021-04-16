from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)

app.secret_key = b"\x91\xd7\x15\x96\xb9=\x8c\x03\xfe\xc0vX\xe9\x14h[\x95\xa8\xaf\xcf>\x1a\x0e\xfb\x0e3\x97/P\x9e\xef9"


@app.route("/")
def index():
    return "Hello World"


@app.route("/about")
def about():
    return render_template("about.html")


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
