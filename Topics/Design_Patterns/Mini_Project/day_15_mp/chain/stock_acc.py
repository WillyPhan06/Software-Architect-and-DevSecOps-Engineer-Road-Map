# chain/stock_acc.py

from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, List
from .market import Market

@dataclass
class StockAccount:
    name: str
    balance: int
    stocks: Dict[str, int] = field(default_factory=dict)

    def receive_notification(self, message):
        print(f"You ({self.name}) received a notification: {message}")

class StockAccountInteraction:
    @staticmethod
    def check_balance_to_order_value(stock_acc: StockAccount, market: Market, quantity: int) -> bool:
        if stock_acc.balance >= market.price*quantity:
            return True
        else:
            return False
        
    @staticmethod
    def check_stock_exist(stock_acc: StockAccount, market: Market):
        if market.tag in stock_acc.stocks:
            return True
        else:
            return False
        
    @staticmethod
    def check_quantity_to_order_quantity(stock_acc: StockAccount, market: Market, quantity: int) -> bool:
        if stock_acc.stocks[market.tag] >= quantity:
            return True
        else:
            return False
        
      
    @staticmethod
    def pull_out_shares(stock_acc: StockAccount, market: Market, quantity: int):
        valid_stock_exist = StockAccountInteraction.check_stock_exist(stock_acc, market)
        valid_quantity_to_order = StockAccountInteraction.check_quantity_to_order_quantity(stock_acc, market, quantity)
        if valid_stock_exist and valid_quantity_to_order:
            stock_acc.stocks[market.tag] -= quantity    
        elif valid_stock_exist:
            print("Can't pull out shares because stock account does not have enough shares")
        else:
            print("Can't pull out shares because stock does not exist in stock account")

    @staticmethod
    def push_in_shares(stock_acc: StockAccount, market: Market, quantity: int):
        if market.tag in stock_acc.stocks:
            stock_acc.stocks[market.tag] += quantity
        else:
            stock_acc.stocks[market.tag] = quantity

    @staticmethod
    def pull_out_money(stock_acc: StockAccount, market: Market, quantity: int):
        if StockAccountInteraction.check_balance_to_order_value(stock_acc, market, quantity):
            stock_acc.balance -= market.price*quantity
        else:
            print("Can't pull out money from stock account because of insufficient amount of money!")

    @staticmethod
    def push_in_money(stock_acc: StockAccount, market: Market, quantity: int):
        stock_acc.balance += market.price*quantity