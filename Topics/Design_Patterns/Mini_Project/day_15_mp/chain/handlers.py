from __future__ import annotations
from .transaction_center import TransactionCenter
from abc import ABC, abstractmethod
from typing import Optional, List
from dataclasses import dataclass, field

class StockHandler(ABC):
    def __init__(self, successor: Optional[StockHandler]=None):
        self.successor = successor

    def set_successor(self, successor: StockHandler):
        self.successor = successor

    @abstractmethod
    def handle(self, request: dict):
        pass

    def process(self, request: dict):
        try:
            order_action = request["type_order"]
            stock_acc = request["stock_acc"]
            market = request["market"]
            quantity = request["quantity"]
            # dispatch to the correct transaction method based on order_action
            if order_action == "buy":
                TransactionCenter.buy_order(stock_acc, market, quantity)
            elif order_action == "sell":
                TransactionCenter.sell_order(stock_acc, market, quantity)
            else:
                print(f"Unknown order action: {order_action}")
            return
        except Exception as e:
            print(f"Error during processing: {e}")

@dataclass
class StateStockHandler(StockHandler):
    state: str = "California"
    # avoid shared mutable default
    counties: List[str] = field(default_factory=lambda: ["Los Angeles", "San Francisco", "Berkeley"])
    

    def handle(self, request: dict):
        user_location = request["location"]
        if  user_location in self.counties:
            print(f"Order processing in {self.state} State Stock Handler")
            self.process(request)
            print(f"Successfully processed in {self.state} State Stock Handler")
            print(f"Sent transaction details to {user_location} County Tax Center")
            return "State_Success"

        elif self.successor:
            print(f"{self.state} State Stock Handler passing request to next handler")
            return self.successor.handle(request)

@dataclass
class NationalStockHandler(StockHandler):
    nation: str = "USA"
    states: List[str] = field(default_factory=lambda: ["California", "Texas", "New York"])

    def handle(self, request: dict):
        user_location = request["location"]
        if  user_location in self.states:
            print(f"Order processing in {self.nation} National Stock Handler")
            self.process(request)
            print(f"Successfully processed in {self.nation} National Stock Handler")
            print(f"Sent transaction details to {user_location} State Tax Center")
            return "National_Success"

        elif self.successor:
            print(f"{self.nation} National Stock Handler passing request to next handler")
            return self.successor.handle(request)

@dataclass
class InternationalStockHandler(StockHandler):
    international: str = "World"
    nations: List[str] = field(default_factory=lambda: ["USA","Vietnam","China"])

    def handle(self, request: dict):
        user_location = request["location"]
        if  user_location in self.nations:
            print(f"Order processing in {self.international} International Stock Handler")
            self.process(request)
            print(f"Successfully processed in {self.international} International Stock Handler")
            print(f"Sent transaction details to {user_location} National Tax Center")
            return "International_Success"

        elif self.successor:
            print(f"{self.international} International Stock Handler passing request to next handler")
            return self.successor.handle(request)

class NoClueStockHandler(StockHandler):
    # signature must match base class: accept a request dict
    def handle(self, request: dict):
        print("We have no absolute clue where you are from")
        # still attempt to process the request as a fallback
        try:
            self.process(request)
            return "NoClue_Success"
        except Exception:
            pass

        