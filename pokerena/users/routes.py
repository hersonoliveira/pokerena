from . import users_blueprint
from flask import render_template, request, current_app
from pokerena.models import User
from sqlalchemy.exc import IntegrityError
from pokerena import db


@users_blueprint.route("/login")
def login():
    return render_template("users/login.html")


@users_blueprint.route("/", methods=["POST"])
def register():
    """
    Register a new user
    ---
    description: user to add to the system
    definitions:
      User:
        type: json
        properties:
            name:
                type: string
            email:
                type: string
            password:
                type: string
    requestBody:
        description: new user to add
        content:
            application/json:
                schema:
                    $ref: '#/definitions/User'
                example:
                    name: DummyUser
                    email: dummy@user.com
                    password: 1234asd
        required: true
    responses:
      201:
        description: User created
    """
    request_data = request.get_json()

    try:
        new_user = User(
            name=request_data["name"],
            email=request_data["email"],
            password=request_data["password"],
        )
        db.session.add(new_user)
        db.session.commit()

        current_app.logger.info(f"New user registered: {request_data['email']}")
        return "New user registered", 201
    except (IntegrityError, ValueError) as e:
        db.session.rollback()
        current_app.logger.error(e)
        return f"Email {request_data['email']} already registered", 400
    except Exception as e:
        return str(e), 500


@users_blueprint.route("/about")
def about():
    return render_template("users/about.html")
