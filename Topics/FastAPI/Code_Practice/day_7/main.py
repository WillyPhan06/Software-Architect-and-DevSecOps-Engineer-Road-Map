from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, field_validator, model_validator, Field
from typing import Annotated, Optional
import errors

app = FastAPI()

class User(BaseModel):
    username: str
    email: EmailStr
    age: int

    @field_validator("username")
    def username_no_spaces(cls, v):
        if " " in v:
            raise ValueError(errors.USERNAME_NO_SPACES)
        return v

    @field_validator("age", mode="before")
    def age_must_be_positive(cls, v):
        if not isinstance(v, int):
            raise ValueError(errors.AGE_MUST_BE_NUMBER)
        if v <= 0:
            raise ValueError(errors.AGE_MUST_BE_POSITIVE)
        return v

class Product(BaseModel):
    code: Annotated[str, Field(pattern=r"^[A-Z]{3}-\d{4}$")]
    name: Annotated[str, Field(min_length=3, max_length=5)]

    @field_validator("name")
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError(errors.NAME_CANNOT_BE_EMPTY)
        return v

class Registration(BaseModel):
    password: str
    password_confirm: str
    referral_code: Optional[str] = None

    @model_validator(mode="before")
    def passwords_match(cls, values: dict):
        if values.get("password") != values.get("password_confirm"):
            raise ValueError(errors.PASSWORDS_MUST_MATCH)
        return values

class Order(BaseModel):
    product_id: int
    quantity: int
    total_price: float

    @model_validator(mode="before")
    def check_total_price(cls, values):
        q = values.get("quantity")
        total = values.get("total_price")
        price_per_unit = 10.0
        if total != q * price_per_unit:
            raise ValueError(errors.TOTAL_PRICE_MISMATCH.format(total=total, quantity=q, price=price_per_unit))
        return values

@app.post("/orders/")
def create_order(order: Order):
    return {"order": order}

@app.post("/register/")
def register_user(reg: Registration):
    return {"user_registered": True}

@app.post("/products/")
def create_product(product: Product):
    return {"product": product}

@app.post("/users/")
def create_user(user: User):
    return {"user": user}
