import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.fake_database import init_test_db


client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_test_db():
    import asyncio
    asyncio.run(init_test_db())

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
