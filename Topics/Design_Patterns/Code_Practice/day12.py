# Initiating and test code with example of drink vending machine as well as applying Decorator Pattern to create a logging to track state change, also implemented refund method for all states logically
# vending/context.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from functools import wraps

class State(ABC):
    @abstractmethod
    def insert_coin(self, ctx: "VendingMachine", amount: int) -> None: ...
    @abstractmethod
    def select_item(self, ctx: "VendingMachine", code: str) -> None: ...
    @abstractmethod
    def dispense(self, ctx: "VendingMachine") -> None: ...

def state_change_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        state = func(*args, **kwargs)
        print(f"State changed to: {state}")
        return state
    return wrapper


class VendingMachine:
    def __init__(self, inventory: Dict[str, Dict]):
        # inventory: code -> {"price": int cents, "stock": int}
        self.inventory = inventory
        self.balance = 0
        self.selected = None
        self.state: State = NoCoinState()

    # public API - delegates to states
    def insert_coin(self, amount: int):
        self.state.insert_coin(self, amount)

    def select_item(self, code: str):
        self.state.select_item(self, code)

    def dispense(self):
        self.state.dispense(self)

    @state_change_log
    def set_state(self, state: State):
        self.state = state
        return self.state

    def refund(self):
        amt = self.balance
        self.balance = 0
        self.selected = None
        print(f"Refunding {amt} cents")
        self.state = NoCoinState()
        return amt

# vending/state_impl.py
class NoCoinState(State):
    def insert_coin(self, ctx: VendingMachine, amount: int):
        ctx.balance += amount
        print(f"Inserted {amount} cents. Balance={ctx.balance}")
        ctx.set_state(HasCoinState())

    def select_item(self, ctx: VendingMachine, code: str):
        print("Insert coin first.")

    def dispense(self, ctx: VendingMachine):
        print("No coin, cannot dispense.")

    def refund(self):
        print("No coin to refund!")

class HasCoinState(State):
    def insert_coin(self, ctx: VendingMachine, amount: int):
        ctx.balance += amount
        print(f"Inserted additional {amount} cents. Balance={ctx.balance}")

    def select_item(self, ctx: VendingMachine, code: str):
        item = ctx.inventory.get(code)
        if not item:
            print("Invalid selection.")
            return
        if item["stock"] <= 0:
            print("Item out of stock.")
            ctx.set_state(NoCoinState())  # or SoldOutState if global
            return
        ctx.selected = code
        if ctx.balance >= item["price"]:
            ctx.set_state(DispensingState())
            ctx.dispense()
        else:
            needed = item["price"] - ctx.balance
            print(f"Need {needed} more cents.")

    def dispense(self, ctx: VendingMachine):
        print("Select item first.")

    def refund(self, ctx: VendingMachine):
        amt = ctx.balance
        ctx.balance = 0
        print(f"Refunding {amt} cents")
        return amt



class DispensingState(State):
    def insert_coin(self, ctx: VendingMachine, amount: int):
        print("Already dispensing, please wait.")

    def select_item(self, ctx: VendingMachine, code: str):
        print("Already dispensing.")

    def dispense(self, ctx: VendingMachine):
        code = ctx.selected
        if not code:
            print("Nothing selected.")
            ctx.set_state(NoCoinState())
            return
        item = ctx.inventory[code]
        item["stock"] -= 1
        change = ctx.balance - item["price"]
        print(f"Dispensing {code}. Change: {change} cents.")
        ctx.balance = 0
        ctx.selected = None
        # After dispensing, choose next state based on inventory
        any_stock = any(it["stock"] > 0 for it in ctx.inventory.values())
        ctx.set_state(NoCoinState() if any_stock else SoldOutState())

    def refund(self, ctx: VendingMachine):
        print("Cannot refund while dispensing")

class SoldOutState(State):
    def insert_coin(self, ctx: VendingMachine, amount: int):
        print("Sold out — refunding.")
        print(f"Refund: {amount} cents")

    def select_item(self, ctx: VendingMachine, code: str):
        print("Sold out.")

    def dispense(self, ctx: VendingMachine):
        print("Sold out.")

    def refund(self, ctx: VendingMachine):
        print(f"Refunding {ctx.balance} cents")
        amt = ctx.balance
        ctx.balance = 0
        return amt


if __name__ == "__main__":
    inv = {"A1": {"price": 100, "stock": 1}, "B2": {"price": 50, "stock": 2}}
    vm = VendingMachine(inv)
    vm.insert_coin(50)  
    vm.insert_coin(10)
    vm.dispense()  
    vm.select_item("A1")      # informs need 50
    vm.insert_coin(100)
    vm.select_item("A1")
    print("Pre dispense function")
    vm.dispense()
  
