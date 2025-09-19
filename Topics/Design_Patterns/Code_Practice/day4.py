#Coding back from memory and understand from example of Builder Pattern

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Pizza:
    name: str = "Normal"
    size: str = "Medium"
    toppings: List[str] = field(default_factory=list)
    price: float = 0.0

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def name(self, name: str) -> PizzaBuilder:
        self.pizza.name = name
        return self
    
    def size(self, size: str) -> PizzaBuilder:
        self.pizza.size = size
        return self
    
    def toppings(self, toppings: List[str]):
        self.pizza.toppings = toppings
        return self
    
    def price(self, price: float) -> PizzaBuilder:
        self.pizza.price = price
        return self
    
    def build(self) -> Pizza:
        return self.pizza
    
if __name__ == "__main__":
    pizza = (PizzaBuilder()
             .name("Pepperoni")
             .size("Huge")
             .toppings(["Pepperoni", "Cheese", "Tomato Sauce", "Chillies"])
             .price(20.0)
             .build()
    )

    print(pizza)