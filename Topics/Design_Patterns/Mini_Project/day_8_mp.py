#Self coding with a little help from code suggestion to apply Facade Pattern and many other patterns into a complex e-commerce scenario making the code maintainable and extensible through designing elegant architecture

from __future__ import annotations
from typing import Dict
from abc import ABC, abstractmethod

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class ItemBox:
    def __init__(self, name: str, item: Item, price: float, batch_size: int):
        self.name = name
        self.item = item
        self.price = price
        self.batch_size = batch_size

class Cart:
    def __init__(self):
        self.items_amount: Dict[Item, int] = {}

class ItemCartHandler:
    @staticmethod
    def add_item(inv: Inventory, cart: Cart, item: Item, quantity: int):
        if item in inv.stock_amount:
            if inv.stock_amount[item] >= quantity:
                inv.stock_amount[item] -= quantity
                if item in cart.items_amount:
                    cart.items_amount[item] += quantity
                else:
                    cart.items_amount[item] = quantity
        else:
            raise ValueError("Item not in stock")

    @staticmethod
    def remove_item(inv: Inventory, cart: Cart, item: Item, quantity: int):
        if item in cart.items_amount:
            if cart.items_amount[item] >= quantity:
                cart.items_amount[item] -= quantity
                if item in inv.stock_amount:
                    inv.stock_amount[item] += quantity
                else:
                    inv.stock_amount[item] = quantity
            else:
                raise ValueError("Not enough items in cart")
        else:
            raise ValueError("Item not in cart")
        
class CartPriceCalculator:
    @staticmethod
    def calculate_total(cart: Cart) -> float:
        total = 0.0
        for item, quantity in cart.items_amount.items():
            total += item.price * quantity
        return total

class Inventory:
    def __init__(self):
        self.stock_amount: Dict[Item, int] = {}

class InventoryItemBoxHandler:
    @staticmethod
    def add_item(inv: Inventory, item_box: ItemBox, quantity: int):
        if item_box.item in inv.stock_amount:
            inv.stock_amount[item_box.item] += quantity * item_box.batch_size
        else:
            inv.stock_amount[item_box.item] = quantity * item_box.batch_size    


class PaymentGatewayRegistry:
    _gateways: Dict[str, type] = {}

    @classmethod
    def register_gateway(cls, name: str, gateway: type):
        cls._gateways[name] = gateway


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: int, currency: str):
        pass


class PayPalGateway(PaymentGateway):
    def process_payment(self, amount: float, currency: str): return f"Paid {amount} {currency} via PayPal"
PaymentGatewayRegistry.register_gateway("paypal_gateway",PayPalGateway)


class PayoneerGateway(PaymentGateway):
    def process_payment(self, amount: float, currency: str): return f"Paid {amount} {currency} via Payoneer"
PaymentGatewayRegistry.register_gateway("payoneer_gateway",PayoneerGateway)

class Notifier(ABC):
    @abstractmethod
    def notify(self, user: str, message: str):
        pass

class EmailNotifier(Notifier):
    def notify(self, user: str, message: str):
        return f"Email sent to {user}: {message}"

class Logger:
    _log: list[str] = []

    @classmethod
    def log(cls, message: str):
        cls._log.append(message)

class CustomerShoppingFacade:
    def __init__(self, **components):
        self._components = components

    def __getattr__(self, item):
        if item in self._components:
            return self._components[item]
        raise AttributeError(f"No component named {item}")
    
    def buy_items_and_pay(self, user: str, item: Item, quantity: int, cart: Cart, payment_gateway: str, currency: str):
        ItemCartHandler.add_item(self.inventory, cart, item, quantity)
        total = CartPriceCalculator.calculate_total(cart)
        gateway_class = PaymentGatewayRegistry._gateways.get(payment_gateway)
        if not gateway_class:
            raise ValueError("Payment gateway not found")
        gateway = gateway_class()
        payment_status = gateway.process_payment(total, currency)
        print(payment_status)
        print(self.notifier.notify(user, f"Purchase successful: {payment_status}"))
        Logger.log(f"User {user} purchased {quantity} of {item.name} for {total} {currency}")
        print(f"Latest Log: {Logger._log[-1]}")
        
        
    
# Client code
if __name__ == "__main__":
    # Setup inventory
    inv = Inventory()
    item1 = Item("Laptop", 1000.0)
    item2 = Item("Phone", 500.0)
    inv.stock_amount[item1] = 10
    inv.stock_amount[item2] = 20
    item_box = ItemBox("Electronics Box", item1, 950.0, 5)
    InventoryItemBoxHandler.add_item(inv, item_box, 2)  # Adds 10 laptops
    print(f"Inventory after adding item boxes: {inv.stock_amount[item1]} laptops")

    # User
    user = "Alice"
    cart = Cart()
    facade = CustomerShoppingFacade(inventory=inv, notifier=EmailNotifier())
    facade.buy_items_and_pay(user, item1, 3, cart, "paypal_gateway", "USD")
    print(f"Inventory after purchase: {inv.stock_amount[item1]} laptops")