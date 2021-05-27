from datetime import datetime

from flask import current_app, render_template, request
from pokerena import db
from pokerena.models import Game, GamesFact

from . import games_blueprint


@games_blueprint.route("/", methods=["POST"])
def add_game():
    """
    Add a new game
    ---
    description: new game with participants
    definitions:
        Game:
            type: json
            properties:
                game_name:
                    type: string
                description:
                    type: string
                date:
                    type: date
                users:
                    $ref: '#/definitions/Users'
        Users:
            type: array
            items:
                type: object
                properties:
                    user_id:
                        type: int
                    position:
                        type: int
    requestBody:
        description: new game to add
        content:
            application/json:
                schema:
                    $ref: '#/definitions/Game'
                example:
                    game_name: pokerena_test
                    description: a game description
                    date: 2021-05-26
                    users:
                      - user_id: 1
                        position: 1
                      - user_id: 2
                        position: 2
        required: true
    responses:
      201:
        description: Game created
    """
    request_data = request.get_json()

    # Add new game
    new_game = Game(
        name=request_data["game_name"],
        description=request_data["description"],
        date=datetime.fromisoformat(request_data["date"]),
    )

    db.session.add(new_game)
    db.session.commit()

    # Retrive users
    # players_json = request_data["users"]

    # Add game facts
    # new_facts = GamesFact(
    #     game_id=new_game.id
    # )

    current_app.logger.info(f"New game added: {new_game}")

    return f"New game {new_game.name} added", 201


@games_blueprint.route("/", methods=["GET"])
def list_games():
    """
    Get all games
    ---
    """
    games = Game.query.order_by(Game.id).all()
    return render_template("games/games.html", games=games)
