from app import main  # noqa: F401


def test_ping(test_app):
    # Given: the state of the application before the test runs (setup code, fixtures, database state)
    # test_app

    # When: the behavior/logic being tested (code under test)
    response = test_app.get("/ping")

    # Then: the expected outcome, including any side effects (assertions)
    assert response.status_code == 200
    assert response.json() == {
        "ping": "pong",
        "environment": "dev",
        "testing": True,
    }
