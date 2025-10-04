# chain/transaction_center.py

from .stock_acc import StockAccount, StockAccountInteraction
from .market import Market, MarketInteraction


class TransactionCenter:
    @staticmethod
    def buy_order(stock_acc: StockAccount, market: Market, quantity: int):
        valid_balance_to_order_value = StockAccountInteraction.check_balance_to_order_value(stock_acc, market, quantity)
        valid_order_quantity_to_shares = MarketInteraction.check_order_quantity_to_shares(market, quantity)

        if valid_balance_to_order_value and valid_order_quantity_to_shares:
            print(f"Processing buy order of {quantity} shares of {market.tag} for {stock_acc.name}")
            MarketInteraction.pull_out_shares(market, quantity)
            StockAccountInteraction.push_in_shares(stock_acc, market, quantity)
            StockAccountInteraction.pull_out_money(stock_acc, market, quantity)
            print(f"Successfully processed buy order of {quantity} shares of {market.tag} for {stock_acc.name}")
        elif valid_balance_to_order_value:
            print("Order quantity exceeds available market shares") 
        elif valid_order_quantity_to_shares:
            print("Balance not enough to fulfill order!")      
        else:
            print("Invalid order! Not enough balance and invalid order quantity!")

    @staticmethod
    def sell_order(stock_acc: StockAccount, market: Market, quantity: int):
        valid_quantity_to_order_quantity = StockAccountInteraction.check_quantity_to_order_quantity(stock_acc, market, quantity)

        if valid_quantity_to_order_quantity:
            print(f"Processing sell order of {quantity} shares of {market.tag} for {stock_acc.name}")
            MarketInteraction.push_in_shares(market, quantity)
            StockAccountInteraction.pull_out_shares(stock_acc, market, quantity)
            StockAccountInteraction.push_in_money(stock_acc, market, quantity)
            print(f"Successfully processed sell order of {quantity} shares of {market.tag} for {stock_acc.name}")

        else:
            print("Not enough shares for selling!")