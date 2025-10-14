from fastapi import FastAPI
from uuid import UUID
from typing import Optional, List
from fastapi import Query
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    on_offer: bool = False

class UpdateItem(BaseModel):
    price: Optional[float] = None
    on_offer: Optional[bool] = None


class Order(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    address: str = Field(..., min_length=5)


app = FastAPI()


# 2️⃣ Define endpoint
@app.post("/users/{username}/orders")
def create_order(username: str, order: Order, coupon: Optional[str] = Query(None)):
    # Simulate creating an order
    return {
        "user": username,
        "order": order,
        "coupon": coupon,
        "status": "Order received successfully ✅"
    }

@app.put("/items/{item_id}")
def update_item(item_id: int, q: Optional[str] = None, update: UpdateItem = None):
    return {"item_id": item_id, "q": q, "update": update}

@app.post("/items/")
def create_item(item: Item):
    # item is validated and parsed into Item
    return {"created": True, "item": item}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "type": "path_param_example"}

@app.get("/users/{username}/profile")
def user_profile(username: str):
    return {"username": username, "profile": f"Profile of {username}"}


@app.get("/resources/{resource_id}")
def read_resource(resource_id: UUID):
    return {"resource_id": str(resource_id), "type": "uuid_path_param_example"}

@app.get("/search")
def search(q: Optional[str] = None, limit: int = 10, tags: Optional[List[str]] = Query(min_length=3)):
    return {"q": q, "limit": limit, "tags": tags}