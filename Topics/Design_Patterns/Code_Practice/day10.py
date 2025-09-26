# Instantiate and test with all cases of strategies

# strategy_oop.py
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, subtotal: float, items: List[str]) -> float:
        """Return discount amount (not final price)."""

@dataclass
class NoDiscount(DiscountStrategy):
    def apply(self, subtotal: float, items: List[str]) -> float:
        return 0.0

@dataclass
class PercentageDiscount(DiscountStrategy):
    percent: float  # e.g., 10 for 10%
    def apply(self, subtotal: float, items: List[str]) -> float:
        return subtotal * (self.percent / 100.0)

@dataclass
class BulkDiscount(DiscountStrategy):
    threshold: int
    discount_per_item: float
    def apply(self, subtotal: float, items: List[str]) -> float:
        if len(items) >= self.threshold:
            return len(items) * self.discount_per_item
        return 0.0

# Context
@dataclass
class PricingEngine:
    strategy: DiscountStrategy

    def price(self, subtotal: float, items: List[str]) -> float:
        discount = self.strategy.apply(subtotal, items)
        return max(subtotal - discount, 0.0)


if __name__ == "__main__":
    engine = PricingEngine(NoDiscount())
    engine_2 = PricingEngine(PercentageDiscount(20))
    engine_3 = PricingEngine(BulkDiscount(5,5))
    engine_4 = PricingEngine(BulkDiscount(5,5))

    list_not_enough = ["nah"]
    list_enough = ["yessir"] * 10

    print(engine.price(100, list_enough))
    print(engine_2.price(100,list_enough))
    print(engine_3.price(100,list_not_enough))
    print(engine_4.price(100,list_enough))




