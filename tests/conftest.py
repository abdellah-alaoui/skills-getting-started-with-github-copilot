from copy import deepcopy

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


def pytest_configure() -> None:
    # Ensure tests import the application with consistent module state
    pass


@pytest.fixture
def client() -> TestClient:
    original_state = deepcopy(activities)
    with TestClient(app) as client:
        yield client
    activities.clear()
    activities.update(original_state)
