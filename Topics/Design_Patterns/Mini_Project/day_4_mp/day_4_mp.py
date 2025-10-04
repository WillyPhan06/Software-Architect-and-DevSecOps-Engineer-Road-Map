#Now mixing Factory and Builder Pattern

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
    
class PizzaFactory:
        _pizza_count = 0
        @staticmethod
        def create_pepperoni_pizza() -> Pizza:
            PizzaFactory._pizza_count += 1
            return (PizzaBuilder()
                    .name("Pepperoni")
                    .size("Huge")
                    .toppings(["Pepperoni", "Cheese", "Tomato Sauce", "Chillies"])
                    .price(20.0)
                    .build()
            )
        
        @staticmethod
        def create_veggie_pizza() -> Pizza:
            PizzaFactory._pizza_count += 1
            return (PizzaBuilder()
                    .name("Veggie Delight")
                    .size("Large")
                    .toppings(["Bell Peppers", "Olives", "Onions", "Mushrooms", "Cheese", "Tomato Sauce"])
                    .price(18.0)
                    .build()
            )
    
if __name__ == "__main__":
    pizza = PizzaFactory.create_pepperoni_pizza()
    print(pizza)
    
    veggie_pizza = PizzaFactory.create_veggie_pizza()
    print(veggie_pizza)
    
    print(f"Total pizzas created: {PizzaFactory._pizza_count}")


