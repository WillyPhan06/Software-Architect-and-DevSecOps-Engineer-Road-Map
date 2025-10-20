import pytest
from fastapi.testclient import TestClient
from main import app
import errors

client = TestClient(app)

# ----------------------------
# User tests
# ----------------------------
def test_create_user_success():
    payload = {"username": "NoobMaster", "email": "test@example.com", "age": 25}
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"user": payload}

def test_create_user_invalid_username():
    payload = {"username": "Noob Master", "email": "test@example.com", "age": 25}
    response = client.post("/users/", json=payload)
    assert response.status_code == 422
    assert errors.USERNAME_NO_SPACES in response.text

def test_create_user_negative_age():
    payload = {"username": "NoobMaster", "email": "test@example.com", "age": -1}
    response = client.post("/users/", json=payload)
    assert response.status_code == 422
    assert errors.AGE_MUST_BE_POSITIVE in response.text

# ----------------------------
# Product tests
# ----------------------------
def test_create_product_success():
    payload = {"code": "ABC-1234", "name": "Prod"}
    response = client.post("/products/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"product": payload}

def test_create_product_invalid_code():
    payload = {"code": "abc-1234", "name": "Prod"}
    response = client.post("/products/", json=payload)
    assert response.status_code == 422
    assert errors.CODE_INVALID_PATTERN in response.text

def test_create_product_name_too_short():
    payload = {"code": "XYZ-9876", "name": "A"}
    response = client.post("/products/", json=payload)
    assert response.status_code == 422
    assert errors.NAME_TOO_SHORT in response.text

# ----------------------------
# Registration tests
# ----------------------------
def test_register_success():
    payload = {"password": "1234", "password_confirm": "1234"}
    response = client.post("/register/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"user_registered": True}

def test_register_password_mismatch():
    payload = {"password": "1234", "password_confirm": "abcd"}
    response = client.post("/register/", json=payload)
    assert response.status_code == 422
    assert errors.PASSWORDS_MUST_MATCH in response.text

# ----------------------------
# Order tests
# ----------------------------
def test_create_order_success():
    payload = {"product_id": 1, "quantity": 3, "total_price": 30.0}
    response = client.post("/orders/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"order": payload}

def test_create_order_invalid_total():
    payload = {"product_id": 1, "quantity": 3, "total_price": 25.0}
    response = client.post("/orders/", json=payload)
    assert response.status_code == 422
    assert "total_price 25.0 doesn't match quantity 3 * price 10.0" in response.text
