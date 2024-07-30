from fastapi.testclient import TestClient
from app.tests.db import app, test_db
from app.tests.db import TestingSessionLocal
from app.tests.factory import user_factory, company_factory

client = TestClient(app)


def test_create_job(test_db):
    db = TestingSessionLocal()
    user = user_factory(db)
    company = company_factory(db)

    response = client.post(
        "/api/v1/jobs",
        json={
            "title": "test job",
            "description": "test description",
            "stage": "test stage",
            "location": "test location",
            "company_id": company.id,
            "user_id": user.id,
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test job"
    assert data["description"] == "test description"
    assert data["stage"] == "test stage"
    assert data["location"] == "test location"
    assert data["company_id"] == company.id
    assert data["user_id"] == user.id
    assert "id" in data


def test_list_jobs(test_db):
    db = TestingSessionLocal()
    user = user_factory(db)
    company = company_factory(db)

    for i in range(10):
        client.post(
            "/api/v1/jobs",
            json={
                "title": f"test job {i}",
                "description": f"test description {i}",
                "stage": f"test stage {i}",
                "location": f"test location {i}",
                "company_id": company.id,
                "user_id": user.id,
            },
        )

    response = client.get("/api/v1/jobs")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["total"] == 10
    assert len(data["items"]) == 10
    assert data["items"][0]["title"] == "test job 0"
    assert data["items"][0]["description"] == "test description 0"
    assert data["items"][0]["stage"] == "test stage 0"
    assert data["items"][0]["location"] == "test location 0"
    assert data["items"][0]["company_id"] == company.id
    assert data["items"][0]["user_id"] == user.id
    assert "id" in data["items"][0]
