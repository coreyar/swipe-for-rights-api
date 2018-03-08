from apistar.test import TestClient
from app import app


def test_http_request(client):
    """
    Testing a view, using the test client.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to API Star!'}
