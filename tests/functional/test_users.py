def test_get_registration_page(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    response = test_client.get("users/register")
    assert response.status_code == 200


def test_valid_registration(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    response = test_client.post(
        "users/register",
        data={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200


def test_invalid_registration(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    response = test_client.post(
        "users/register",
        data={
            "name": "test_user",
            "email": "test@test.com",
            "password": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200


def test_duplicate_registration(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    test_client.post(
        "users/register",
        data={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
    )
    response = test_client.post(
        "users/register",
        data={
            "name": "test_user",
            "email": "test@test.com",
            "password": "Flask1234",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
