# strategy_pythonic_example.py
from typing import Protocol, List

# Strategy protocol
class DiscountFn(Protocol):
    def __call__(self, subtotal: float, items: List[str]) -> float: ...

# Factory functions for strategies
def no_discount_fn() -> DiscountFn:
    def f(subtotal: float, items: List[str]) -> float:
        return 0.0
    return f

def percentage_fn(percent: float) -> DiscountFn:
    def f(subtotal: float, items: List[str]) -> float:
        return subtotal * (percent / 100.0)
    return f

def bulk_fn(threshold: int, discount_per_item: float) -> DiscountFn:
    def f(subtotal: float, items: List[str]) -> float:
        return len(items) * discount_per_item if len(items) >= threshold else 0.0
    return f

# Context function
def price_with_strategy(strategy: DiscountFn, subtotal: float, items: List[str]) -> float:
    discount = strategy(subtotal, items)
    return max(subtotal - discount, 0.0)

# Testing all strategies
if __name__ == "__main__":
    items_small = ["apple", "banana"]            # 2 items
    items_large = ["apple", "banana", "orange", "pear", "grape", "melon"]  # 6 items
    subtotal = 100.0

    # Instantiate strategies
    no_disc = no_discount_fn()
    perc_disc = percentage_fn(20)  # 20% discount
    bulk_disc = bulk_fn(threshold=5, discount_per_item=5)  # 5+ items → $5 off per item

    # Test each strategy
    print("=== No Discount ===")
    print(f"Small list: {price_with_strategy(no_disc, subtotal, items_small)}")
    print(f"Large list: {price_with_strategy(no_disc, subtotal, items_large)}\n")

    print("=== Percentage Discount (20%) ===")
    print(f"Small list: {price_with_strategy(perc_disc, subtotal, items_small)}")
    print(f"Large list: {price_with_strategy(perc_disc, subtotal, items_large)}\n")

    print("=== Bulk Discount (threshold 5, $5 per item) ===")
    print(f"Small list: {price_with_strategy(bulk_disc, subtotal, items_small)}")
    print(f"Large list: {price_with_strategy(bulk_disc, subtotal, items_large)}")
