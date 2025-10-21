from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": [f"item{i}" for i in range(skip, skip+limit)]}
