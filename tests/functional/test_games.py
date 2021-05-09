def test_post_add_new_game(test_client):
    """
    GIVEN a flask app
    WHEN the '/add_game' is POST
    THEN check endpoint is success
    """
    response = test_client.post(
        "/add_game",
        data={
            "game_name": "test-game",
            "description": "dummy game",
            "date": "2021-05-27"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
