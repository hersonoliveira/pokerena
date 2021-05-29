def test_valid_registration(test_client):
    """
    GIVEN a Flask app
    WHEN the endpoint 'users/' POST one valid user
    THEN user is created (HTTP code 201 returned)
    """
    response = test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
    )
    assert response.status_code == 201


def test_invalid_registration(test_client):
    """
    GIVEN a Flask app
    WHEN the endpoint 'users/' POST user missing password
    THEN HTTP Bad request error is returned
    """
    response = test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test@test.com",
            "password": "",
        },
    )
    assert response.status_code == 400


def test_duplicate_registration(test_client):
    """
    GIVEN a Flask app
    WHEN the endpoint 'users/' POST two valid equal users
    THEN HTTP Bad request error is returned
    """
    test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
    )
    response = test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
    )
    assert response.status_code == 400


def test_get_all_users(test_client):
    """
    GIVEN a Flask app
    WHEN the endpoint 'users/' POST two valid diff users
    THEN a new user is created (HTTP response 200)
    """
    test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
    )
    test_client.post(
        "users/",
        json={
            "name": "test_user",
            "email": "test1@test.com",
            "password": "Flask1234",
        },
    )
    response = test_client.get("users/")

    assert response.status_code == 200
    assert (
        response.data
        == b'{"test1@test.com":"test_user","test@test.com":"test_user"}\n'
    )
