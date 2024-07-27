from fastapi.testclient import TestClient
from app.tests.db import app, override_get_db
from app.contexts import users
from app.schemas import UserCreate

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


def test_login_user():
    email = "deadpool@example.com"
    password = "chimichangas4life"

    response = client.post(
        "/api/v1/users",
        json={"email": email, "password": password},
    )

    response = client.post(
        "/api/v1/users/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == email
