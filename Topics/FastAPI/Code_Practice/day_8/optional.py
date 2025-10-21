from typing import Optional
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

def validate_prices(min_price: Optional[float], max_price: Optional[float]):
    if min_price is not None and max_price is not None:
        if max_price < min_price:
            raise HTTPException(
                status_code=400,
                detail="max_price must be greater than or equal to min_price"
            )
        
def validate_results(results: list):
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No items found matching the criteria"
        )

fake_products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 1200},
    {"id": 2, "name": "Book", "category": "books", "price": 15},
    {"id": 3, "name": "Phone", "category": "electronics", "price": 800},
]

@app.get("/products/filter/")
def filter_products(category: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    results = fake_products
    if category:
        results = [p for p in results if p["category"] == category]
    if min_price:
        results = [p for p in results if p["price"] >= min_price]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    validate_results(results)
    return results


@app.get("/search/")
def search_items(q: Optional[str] = None):
    if q:
        return {"results": [f"Found {q}"]}
    return {"results": ["No query provided"]}

@app.get("/filter/")
def filter_items(category: str, min_price: Optional[float] = None, max_price: Optional[float] = None):
    validate_prices(min_price, max_price)
    return {"category": category, "min_price": min_price, "max_price": max_price}

@app.get("/products/")
def get_products(
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="Search term"),
    limit: int = Query(10, ge=1, le=100, description="Number of items to return")
):
    return {"q": q, "limit": limit}

