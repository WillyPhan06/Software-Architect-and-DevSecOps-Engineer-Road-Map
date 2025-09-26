# Using mini project from Observer Pattern day to enhance and apply Strategy Pattern more into it
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List

class PaymentGate(ABC):
    @abstractmethod
    def announce_processed_payment(self, message: str):
        pass

class PaypalGate(PaymentGate):
    def announce_processed_payment(self, message):
        print(f"Paypal Announce: {message}")

class PayoneerGate(PaymentGate):
    def announce_processed_payment(self, message):
        print(f"Payoneer Announce: {message}")

@dataclass
class Market(ABC):
    shares: int
    price: float
    tag: str = None

@dataclass
class AppleMarket(Market):
    shares: int
    price: float
    tag: str = "AAPL"

@dataclass
class TeslaMarket(Market):
    shares: int
    price: float
    tag: str = "TSLA"

@dataclass
class MicrosoftMarket(Market):
    shares: int
    price: float
    tag: str = "MSFT"

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
        
        
class MarketInteraction:
    @staticmethod
    def check_order_quantity_to_shares(market: Market, quantity: int):
        if market.shares >= quantity:
            return True
        else:
            return False
        
    @staticmethod
    def pull_out_shares(market: Market, quantity: int):
        market.shares -= quantity

    @staticmethod
    def push_in_shares(market: Market, quantity: int):
        market.shares += quantity
        
@dataclass
class NotificationCenter:
    accounts: List[StockAccount] = field(default_factory=list)

    def add_acc_for_notify(self, stock_acc: StockAccount):
        self.accounts.append(stock_acc)   

    def notify(self, message: str):
        for account in self.accounts:
            account.receive_notification(message)    

class TransactionCenter:
    @staticmethod
    def buy_order(stock_acc: StockAccount, market: Market, quantity: int, paymentgate: PaymentGate):
        valid_balance_to_order_value = StockAccountInteraction.check_balance_to_order_value(stock_acc, market, quantity)
        valid_order_quantity_to_shares = MarketInteraction.check_order_quantity_to_shares(market, quantity)

        if valid_balance_to_order_value and valid_order_quantity_to_shares:
            print(f"Processing buy order of {quantity} shares of {market.tag} for {stock_acc.name}")
            MarketInteraction.pull_out_shares(market, quantity)
            StockAccountInteraction.push_in_shares(stock_acc, market, quantity)
            StockAccountInteraction.pull_out_money(stock_acc, market, quantity)
            buy_order_stat = f"Successfully processed buy order of {quantity} shares of {market.tag} for {stock_acc.name}"
            paymentgate.announce_processed_payment(buy_order_stat)
        elif valid_balance_to_order_value:
            print("Order quantity exceeds available market shares") 
        elif valid_order_quantity_to_shares:
            print("Balance not enough to fulfill order!")      
        else:
            print("Invalid order! Not enough balance and invalid order quantity!")

    @staticmethod
    def sell_order(stock_acc: StockAccount, market: Market, quantity: int, paymentgate: PaymentGate):
        valid_quantity_to_order_quantity = StockAccountInteraction.check_quantity_to_order_quantity(stock_acc, market, quantity)

        if valid_quantity_to_order_quantity:
            print(f"Processing sell order of {quantity} shares of {market.tag} for {stock_acc.name}")
            MarketInteraction.push_in_shares(market, quantity)
            StockAccountInteraction.pull_out_shares(stock_acc, market, quantity)
            StockAccountInteraction.push_in_money(stock_acc, market, quantity)
            sell_order_stat = f"Successfully processed sell order of {quantity} shares of {market.tag} for {stock_acc.name}"
            paymentgate.announce_processed_payment(sell_order_stat)

        else:
            print("Not enough shares for selling!")

if __name__ == "__main__":
    my_account = StockAccount("Will", 1000)
    apple_market = AppleMarket(1000,10)
    paypal = PaypalGate()
    payoneer = PayoneerGate()

    print("-----------------------------------------------")
    TransactionCenter.buy_order(my_account,apple_market,50, paypal)
    print(f"Balance: {my_account.balance}")
    print(f"Shares: {my_account.stocks}")
    print("-----------------------------------------------")
    TransactionCenter.sell_order(my_account, apple_market, 50, payoneer)
    print(f"Balance: {my_account.balance}")
    print(f"Shares: {my_account.stocks}")
    print("-----------------------------------------------")
    notify = NotificationCenter()
    notify.add_acc_for_notify(my_account)
    notify.notify("Why am I still here just to suffer")

    

