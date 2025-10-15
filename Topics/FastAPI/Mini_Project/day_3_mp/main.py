from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, PositiveInt, constr, field_validator, model_validator
from typing import Optional, List
from enum import Enum
import re
import uuid

app = FastAPI()

# ---- Helper types ----
ShortStr = constr(min_length=2, max_length=10)

# ---- Enums ----
class Role(str, Enum):
    admin = "admin_here"
    user = "user_here"
    guest = "guest_here"

# ---- Models ----
class Profile(BaseModel):
    nickname: Optional[ShortStr] = None
    role: Role = Role.user
    reputation: PositiveInt = 1

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    active: bool = True
    score: float = Field(0.0, ge=0, le=100)

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Item(BaseModel):
    name: str
    price: float
    quantity: int


class Order(BaseModel):
    items: List[Item]
    declared_total: float
    coupon_code: Optional[str] = Field(None, pattern=r"^[A-Z0-9]{6}$")

    @model_validator(mode="after")
    def check_declared_total(self):
        subtotal = sum(item.price * item.quantity for item in self.items)
        if abs(subtotal - self.declared_total) > 0.01:
            raise ValueError("Declared total does not match computed subtotal")
        return self


@app.post("/checkout/")
def checkout(order: Order):
    subtotal = sum(item.price * item.quantity for item in order.items)
    discount = 0.0

    if order.coupon_code:
        if not re.fullmatch(r"^[A-Z0-9]{6}$", order.coupon_code):
            raise HTTPException(status_code=400, detail="Invalid coupon code format")
        if order.coupon_code == "TENOFF":
            discount = 0.1 * subtotal

    total = subtotal - discount
    return {
        "order_id": str(uuid.uuid4()),
        "subtotal": subtotal,
        "discount": discount,
        "total": total,
    }
