from app import login
from flask_mysqldb import MySQL


def test_index():
    assert login() == "Login via the login Form"