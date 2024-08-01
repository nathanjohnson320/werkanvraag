from fastapi.testclient import TestClient
from app.tests.db import app, test_db

client = TestClient(app)


def test_auth_user(test_db):
    email = "deadpool@example.com"
    password = "chimichangas4life"

    client.post("/api/v1/users", json={"email": email, "password": password})

    response = client.post(
        "/api/v1/users/token",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["access_token"] != None
    assert data["token_type"] == "bearer"

    response = client.get(
        "/api/v1/users/me", headers={"Authorization": f"Bearer {data['access_token']}"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == email
