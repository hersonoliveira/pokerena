from flask import Flask, render_template, request


app = Flask(__name__)


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
    return render_template("add_game.html")
