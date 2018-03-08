from apistar.test import TestClient
import pytest

from app import app


@pytest.fixture(scope="session")
def client():
    """Use a single TestClient per test suite run"""
    return TestClient(app)
