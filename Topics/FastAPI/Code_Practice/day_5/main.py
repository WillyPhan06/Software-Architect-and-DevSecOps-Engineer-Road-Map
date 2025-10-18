from fastapi import FastAPI, Depends, Query, HTTPException, status, Header
from typing import Generator

app = FastAPI()

def get_db() -> Generator:
    db = {"connected": False, "authorized": False}  # pretend DB connection
    try:
        yield db
    finally:
        print("Closing DB connection...")  # cleanup


# dependency that reads the api_key from the query string and validates it
def get_api_key(api_key: str | None = Query(None)):
    # simulate "missing"
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API key",
        )

    # simulate "invalid"
    if api_key != "my-secret-api-key":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
        )

    # valid -> return it to the endpoint
    return api_key

def valid_limit(limit: int = Query(10, ge=1, le=100)):
    if limit > 50:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Limit too high")
    return limit

def get_current_user(x_token: str = Header(...)):
    if x_token != "fake-super-secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "willy"}

@app.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.get("/items/")
def list_items(limit: int = Depends(valid_limit)):
    return {"limit": limit, "items": ["item1"] * limit}

@app.get("/check-api")
def check_api(api_key: str = Depends(get_api_key)):
    return {"api_key": api_key}

@app.get("/users/")
def get_users(db = Depends(get_db)):
    if not db["connected"]:
        raise HTTPException(500, "DB not connected")
    if not db["authorized"]:
        raise HTTPException(401, "DB not authorized")
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

