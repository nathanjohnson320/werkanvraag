from fastapi.testclient import TestClient
from app.tests.db import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/api/v1/users",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
