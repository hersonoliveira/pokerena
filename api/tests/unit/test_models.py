
def test_new_user(new_user):
    """
    GIVEN the user model
    WHEN a new user is created
    THEN check email is valid and hashed password does not equal to the one provided
    """
    assert new_user.name == "dummy_user"
    assert new_user.email == "dummy@me.com"
    assert new_user.password_hashed != "1234"
