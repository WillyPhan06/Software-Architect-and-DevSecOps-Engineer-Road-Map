from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_Item_product():
    response = client.get('/products')
    products = response.json()
    assert any(product['name'] == 'Item' for product in products)
