from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_list_users_returns_ok():
    response = client.get("/api/users")

    assert response.status_code == 200


def test_list_users_returns_exact_users():
    response = client.get("/api/users")

    assert response.json() == [
        {"id": 1, "name": "Juan Pérez"},
        {"id": 2, "name": "Ana García"},
    ]
