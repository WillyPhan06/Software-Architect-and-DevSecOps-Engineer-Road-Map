# filename: main.py
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import RedirectResponse

# -------------------------------
# Pydantic model for items
# -------------------------------
class Item(BaseModel):
    name: str = Field(..., example="Laptop")
    price: float = Field(..., example=999.99)
    description: Optional[str] = Field(None, example="A high-end gaming laptop")
    on_offer: Optional[bool] = Field(False, example=True)

# -------------------------------
# Tags metadata
# -------------------------------
tags_metadata = [
    {
        "name": "Root",
        "description": "Root endpoint and general information"
    },
    {
        "name": "Items",
        "description": "Operations with items, including retrieving details"
    }
]

# -------------------------------
# Create FastAPI app
# -------------------------------
app = FastAPI(
    title="My Awesome API",
    description="This is a sample API built with FastAPI. It demonstrates GET endpoints with path and query parameters.",
    version="1.0.0",
    contact={
        "name": "Willy Phan",
        "url": "https://example.com/contact",
        "email": "willy@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=tags_metadata,
    docs_url="/drip"
)

# -------------------------------
# Version 1 router
# -------------------------------
v1_router = APIRouter(prefix="/v1")

@v1_router.get("/", response_model=dict, tags=["Root"], summary="Why bud here", description="Very long")
def read_root_v1():
    """
    Root endpoint returning a welcome message for API v1.
    """
    return {"message": "Hello, World! (v1)"}

@v1_router.get("/items/{item_id}", response_model=Item, tags=["Items"], responses={
    404: {"description": "Item not found"}
})
def read_item_v1(item_id: int, q: Optional[str] = None):
    """
    Get an item by ID (v1).
    """
    example_item = Item(
        name="Example Item",
        price=42.0,
        description=f"This is item #{item_id}, query={q}",
        on_offer=True
    )
    return example_item

# -------------------------------
# Version 2 router
# -------------------------------
v2_router = APIRouter(prefix="/v2")

@v2_router.get("/", response_model=dict, tags=["Root"])
def read_root_v2():
    """
    Root endpoint returning a welcome message for API v2.
    """
    return {"message": "Hello, World! (v2)"}

@v2_router.get("/items/{item_id}", response_model=Item, tags=["Items"], responses={
    404: {"description": "Item not found"}
})
def read_item_v2(item_id: int, q: Optional[str] = None):
    """
    Get an item by ID (v2). In v2 we might add new features or fields.
    """
    example_item = Item(
        name=f"Example Item v2-{item_id}",
        price=42.0,
        description=f"This is item #{item_id} with query={q} (v2)",
        on_offer=False
    )
    return example_item

@app.get("/old-endpoint", deprecated=True)
def old():
    pass

@app.get("/items/{item_id}", include_in_schema=False)
def redirect_to_v1(item_id: int, q: Optional[str] = None):
    """
    Redirect to v1 if version prefix not specified.
    """
    target_url = f"/v1/items/{item_id}"
    if q:
        target_url += f"?q={q}"
    return RedirectResponse(url=target_url)


# -------------------------------
# Include routers in app
# -------------------------------
app.include_router(v1_router)
app.include_router(v1_router, prefix="")  # /items, / (defaults to v1)
app.include_router(v2_router)
