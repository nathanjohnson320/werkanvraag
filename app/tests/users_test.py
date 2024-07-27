from fastapi.testclient import TestClient
from app.tests.db import app, test_db


client = TestClient(app)


def test_create_user(test_db):
    response = client.post(
        "/api/v1/users",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data


def test_login_user(test_db):
    email = "deadpool@example.com"
    password = "chimichangas4life"

    client.post("/api/v1/users", json={"email": email, "password": password})

    response = client.post(
        "/api/v1/users/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == email


def test_login_user_wrong_password(test_db):
    email = "deadpool@example.com"
    password = "chimichangas4life"

    client.post("/api/v1/users", json={"email": email, "password": password})

    response = client.post(
        "/api/v1/users/login",
        json={"email": email, "password": "banana"},
    )
    assert response.status_code == 400, response.text


def test_list_users(test_db):
    for i in range(10):
        client.post(
            "/api/v1/users", json={"email": f"test{i}@test.com", "password": "testing"}
        )

    response = client.get("/api/v1/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["total"] == 10
    assert len(data["items"]) == 10
    assert data["items"][0]["email"] == "test0@test.com"
