from app import hello


def test_index():
    assert hello() == "Hello, World!"