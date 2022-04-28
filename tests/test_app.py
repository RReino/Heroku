from app import login


def test_index():
    assert login() == "Login via the login Form"