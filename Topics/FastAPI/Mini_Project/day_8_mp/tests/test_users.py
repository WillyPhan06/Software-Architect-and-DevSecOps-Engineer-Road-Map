from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_users():
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_Willy_user():
    response = client.get('/users')
    users = response.json()
    assert any(user['name'] == 'Willy' for user in users)
