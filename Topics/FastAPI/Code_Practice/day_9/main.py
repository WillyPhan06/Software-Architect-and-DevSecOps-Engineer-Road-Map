from fastapi import FastAPI

app = FastAPI()

@app.get("/users/")
@app.get("/all-users/")  # multiple paths
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/items/special")
def read_special_item():
    return {"item": "special"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/products/{product_id:int}")
def get_product(product_id: int):
    return {"product_id": product_id}

@app.get("/products/latest")
def get_latest_product():
    return {"product": "latest"}

def isValidMonth(month: int) -> bool:
    return 1 <= month <= 12


@app.get("/reports/summary")
@app.get("/reports/{year:int}/{month:int}")
@app.get("/reports/{year:int}")
def get_report(year: int = None, month: int = None):
    if month is not None and isValidMonth(month):
        return {"report": f"{year}-{month}"}
    elif month is not None:
        return {"error": "Invalid month lil bro"}
    elif year is not None:
        return {"report": f"{year}"}
    else:
        return {"report": "WHAT BRO"}


