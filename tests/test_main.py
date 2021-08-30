from api import main


def test_hello() -> None:
    assert main.hello() == {"message": "Hello"}
