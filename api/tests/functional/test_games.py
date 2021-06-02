def test_post_add_new_game(test_client):
    """
    GIVEN a flask app
    WHEN the '/games' is POST
    THEN new game is created, HTTP response 201
    """
    response = test_client.post(
        "/games",
        json={
            "game_name": "test-game",
            "description": "dummy game",
            "date": "2021-05-27",
            "users": [
                {
                    "user_id": 1,
                    "position": 1,
                    "rebuy": 1,
                    "add_on": True
                },
                {
                    "user_id": 2,
                    "position": 2,
                    "rebuy": 1,
                    "add_on": True
                },
                {
                    "user_id": 3,
                    "position": 3,
                    "rebuy": 1,
                    "add_on": True
                }
            ]
        },
        follow_redirects=True
    )

    assert response.status_code == 201


def test_get_all_games(populate_db):
    """
    GIVEN a flask app
    WHEN the '/games' is GET
    THEN return all games
    """
    response = populate_db.get(
        "games/"
    )

    assert response.status_code == 200
    assert response.data == b'[{"id": 1, "name": "pokerena", "description": "Dummy game", "date": "2021-05-27T00:00:00"}]'
