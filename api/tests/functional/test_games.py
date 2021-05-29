def test_post_add_new_game(test_client):
    """
    GIVEN a flask app
    WHEN the '/games' is POST
    THEN check endpoint is success
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
