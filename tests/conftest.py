import os

import pytest
from starlette.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")  # scope="module" means this fixture will run once per test module
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = (
        get_settings_override  # Replaces get_settings with get_settings_override
    )
    with TestClient(main.app) as test_client:
        # testing
        yield test_client

    # tear down
