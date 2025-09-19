#This time Builder Pattern but with Immutable Data Class by freezing and whenever you wanna change something you just create a new instance with replace function

from __future__ import annotations
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Car: 
    brand: str = "Toyota"
    model: str = "Corolla"
    color: str = "White"
    year: int = 2020
    price: float = 20000.0

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def brand(self, brand: str) -> CarBuilder:
        self.car = replace(self.car, brand=brand)
        return self
    
    def model(self, model: str) -> CarBuilder:
        self.car = replace(self.car, model=model)
        return self
    
    def color(self, color: str) -> CarBuilder:
        self.car = replace(self.car, color=color)
        return self
    
    def year(self, year: int) -> CarBuilder:
        self.car = replace(self.car, year=year)
        return self
    
    def price(self, price: float) -> CarBuilder:
        self.car = replace(self.car, price=price)
        return self
    
    def build(self) -> Car:
        return self.car
    
if __name__ == "__main__":
    car = (CarBuilder()
           .brand("Honda")
           .model("Civic")
           .color("Red")
           .year(2022)
           .price(25000.0)
           .build()
    )

    print(car)
