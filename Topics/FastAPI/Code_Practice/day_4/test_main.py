from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_missing_item():
    r = client.get("/items/999")
    assert r.status_code == 404
    assert r.json() == {"detail": "Item not found"}


def test_out_of_stock():
    r = client.post("/buy/10")
    assert r.status_code == 400
    assert r.json()["error"] == "out_of_stock"
