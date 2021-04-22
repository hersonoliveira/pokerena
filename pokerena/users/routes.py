from . import users_blueprint
from flask import render_template


@users_blueprint.route("/login")
def login():
    return render_template("users/login.html")


@users_blueprint.route("/signup")
def signup():
    return render_template("users/signup.html")


@users_blueprint.route("/about")
def about():
    return render_template("users/about.html")
