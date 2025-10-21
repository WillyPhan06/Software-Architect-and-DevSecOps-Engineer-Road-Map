import os

# Base project structure
folders = [
    "data_objects",
    "end_points",
    "helper_functions",
    "tests"
]

# Files to create in each folder
files = {
    "data_objects": ["user.py", "product.py"],
    "end_points": ["users.py", "products.py"],
    "helper_functions": ["db_helper.py", "auth_helper.py"],
    "tests": ["test_users.py", "test_products.py"],
    "root": ["main.py"]
}

# File templates
templates = {
    "data_objects/user.py": """from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
""",
    "data_objects/product.py": """from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
""",
    "end_points/users.py": """from fastapi import APIRouter

from data_objects.user import User

router = APIRouter()

@router.get('/users')
def get_users():
    return [User(id=1, name='Willy').dict()]
""",
    "end_points/products.py": """from fastapi import APIRouter

from data_objects.product import Product

router = APIRouter()

@router.get('/products')
def get_products():
    return [Product(id=1, name='Item', price=9.99).dict()]
""",
    "helper_functions/db_helper.py": """def connect_db():
    # Dummy DB connection
    return "Connected to DB"
""",
    "helper_functions/auth_helper.py": """def check_auth(user_id: int):
    # Dummy auth check
    return True
""",
    "tests/test_users.py": """from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_users():
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
""",
    "tests/test_products.py": """from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
""",
    "main.py": """from fastapi import FastAPI
from end_points.users import router as users_router
from end_points.products import router as products_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
"""
}


for folder, file_list in files.items():
    if folder == "root":
        for file_name in file_list:
            path = file_name
            with open(path, "w") as f:
                f.write(templates.get(file_name, ""))
    else:
        for file_name in file_list:
            path = os.path.join(folder, file_name).replace("\\", "/")  # force forward slashes
            with open(path, "w") as f:
                f.write(templates.get(path, ""))


print("Mini FastAPI project structure created successfully!")
