from fastapi import FastAPI, status, Response, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

app = FastAPI()

class ItemIn(BaseModel):
    name: str
    description: str = None

class UserIn(BaseModel):
    username: str
    password: str   # should never be returned

class UserOut(BaseModel):
    id: int
    username: str
    isHashed: str = "unknown"

class OutOfStockError(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id



@app.post("/users/", response_model=UserOut, response_model_include={"id"}, status_code=201)
def create_user(user: UserIn):
    # pretend we save to DB and get id=1
    db_user = {"id": 1, "username": user.username, "isHashed": "hashed"}
    return db_user   # password will be excluded by response_model
 
@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int):
    # delete logic...
    return None

@app.post("/login")
def login():
    # bad credentials
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail":"Invalid credentials"})

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemIn, response: Response):
    # pretend we save to DB and get id=42
    item_id = 42
    
    # set Location header
    response.headers["Location"] = f"/items/{item_id}"
    
    # optionally return some content
    return {"id": item_id, "name": item.name}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    fake_db = {42: {"id": 42, "name": "Sample Item", "description": "This is a sample item"}}

    item = fake_db.get(item_id)

    if item_id == 69:
        raise HTTPException(status_code=469, detail="How did you do that?")
    if not item:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Reason": "no-access"})
    

    return item


@app.exception_handler(OutOfStockError)
async def out_of_stock_handler(request: Request, exc: OutOfStockError):
    return JSONResponse(
        status_code=400,
        content={"error": "out_of_stock", "product_id": exc.product_id, "message": "Product is out of stock"}
    )

@app.post("/buy/{product_id}")
def buy(product_id: int):
    # pretend stock check
    raise OutOfStockError(product_id)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # build simpler error list
    errors = [{"loc": e["loc"], "msg": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"error": "validation_error", "details": errors})