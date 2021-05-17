def test_valid_registration(test_client):
    """
    GIVEN
    WHEN
    THEN
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
    GIVEN
    WHEN
    THEN
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
    GIVEN
    WHEN
    THEN
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
