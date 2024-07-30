from fastapi.testclient import TestClient
from app.tests.db import app, test_db


client = TestClient(app)


def test_create_company(test_db):
    response = client.post(
        "/api/v1/companies",
        json={"name": "test company"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "test company"
    assert "id" in data


def test_list_companies(test_db):
    for i in range(10):
        client.post("/api/v1/companies", json={"name": f"test company {i}"})

    response = client.get("/api/v1/companies")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["total"] == 10
    assert len(data["items"]) == 10
    assert data["items"][0]["name"] == "test company 0"
