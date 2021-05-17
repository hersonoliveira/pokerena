from . import users_blueprint
from flask import render_template, request, current_app
from pokerena.models import User
from sqlalchemy.exc import IntegrityError
from pokerena import db


@users_blueprint.route("/login")
def login():
    return render_template("users/login.html")


@users_blueprint.route("/register", methods=["POST"])
def register():
    request_data = request.get_json()

    try:
        new_user = User(
            name=request_data["name"],
            email=request_data["email"],
            password=request_data["password"],
        )
        db.session.add(new_user)
        db.session.commit()
    except (IntegrityError, ValueError) as e:
        db.session.rollback()
        current_app.logger.error(e)
        return f"Email {request_data['email']} already registered", 400
    except:
        return "Server error", 500

    current_app.logger.info(f"New user registered: {request_data['email']}")
    return "New user registered", 200


@users_blueprint.route("/about")
def about():
    return render_template("users/about.html")
