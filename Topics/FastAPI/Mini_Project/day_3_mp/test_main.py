from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def sample_order(coupon=None, declared_total=None):
    return {
        "order_id": 1,
        "buyer": {
            "id": 1,
            "username": "willy",
            "email": "willy@example.com"
        },
        "shipping": {
            "street": "123 Street",
            "city": "HCMC",
            "zip_code": "700000"
        },
        "items": [
            {"product_id": 1, "name": "Book", "price": 50.0, "quantity": 2}
        ],
        "declared_total": declared_total,
        "coupon_code": coupon
    }

# ✅ Valid order accepted
def test_valid_order():
    data = sample_order(declared_total=100.0)
    response = client.post("/checkout/", json=data)
    assert response.status_code == 200
    body = response.json()
    assert body["subtotal"] == 100.0
    assert body["discount"] == 0.0
    assert body["total"] == 100.0

# ❌ Declared_total mismatch rejected
def test_declared_total_mismatch():
    data = sample_order(declared_total=50.0)
    response = client.post("/checkout/", json=data)
    assert response.status_code == 422  # validation error from Pydantic

# ✅ Coupon validation works (correct format)
def test_valid_coupon_tenoff():
    data = sample_order(coupon="TENOFF", declared_total=100.0)
    response = client.post("/checkout/", json=data)
    assert response.status_code == 200
    body = response.json()
    assert body["discount"] == 10.0
    assert body["total"] == 90.0

# ❌ Coupon validation works (wrong format)
def test_invalid_coupon_format():
    data = sample_order(coupon="bad_code", declared_total=100.0)
    response = client.post("/checkout/", json=data)
    assert response.status_code == 422  # FastAPI validation error

