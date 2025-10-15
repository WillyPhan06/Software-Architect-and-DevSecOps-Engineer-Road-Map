# main.py
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, PositiveInt, constr, field_validator, model_validator
from typing import Optional, Literal, List
from enum import Enum



# Constrained types

app = FastAPI()

ShortStr = constr(min_length=2, max_length=10)

class Role(str, Enum):
    admin = "admin_here"
    user = "user_here"
    guest = "guest_here"

class Profile(BaseModel):
    nickname: Optional[ShortStr] = None
    role: Role = Role.user
    reputation: PositiveInt = 1

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    active: bool = True
    score: float = Field(0.0, ge=0, le=100)   # ge = >=, le = <=

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Item(BaseModel):
    product_id: int
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(1, gt=0)

class Order(BaseModel):
    order_id: int
    items: List[Item]
    declared_total: Optional[float] = None

    @field_validator("items")
    @classmethod
    def non_empty_items(cls, v):
        if not v or len(v) == 0:
            raise ValueError("order must have at least one item")
        return v

    @model_validator(mode="after")
    def check_total(self):
        items = self.items or []
        declared = self.declared_total
        calc = sum(i.price * i.quantity for i in items)
        if declared is not None and abs(calc - declared) > 1e-6:
            raise ValueError(
                f"declared_total {declared} does not match calculated total {calc}"
            )
        return self

@app.post("/profiles/")
def create_profile(p: Profile):
    return {"profile": p}

@app.post("/users/")
def create_user(user: User):
    return {"ok": True, "user": user}

@app.get("/mode/")
def mode(m: Literal["fast", "safe"] = "safe"):
    return {"mode": m}

@app.post("/orders/")
def create_order(order: Order):
    total = sum(item.price * item.quantity for item in order.items)
    return {"order_id": order.order_id, "total": total}




