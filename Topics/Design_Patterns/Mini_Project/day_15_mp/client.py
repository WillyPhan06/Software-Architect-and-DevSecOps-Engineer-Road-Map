# client.py

from chain.transaction_center import TransactionCenter
from chain.notification import NotificationCenter
from chain.stock_acc import StockAccount
from chain.market import AppleMarket
from chain.handlers import StockHandler, StateStockHandler, NationalStockHandler, InternationalStockHandler, NoClueStockHandler

if __name__ == "__main__":
    my_account = StockAccount("Will", 1000)
    apple_market = AppleMarket(1000,10)
    quantity = 50

    state_sh = StateStockHandler()
    nation_sh = NationalStockHandler()
    international_sh = InternationalStockHandler()
    no_clue_sh = NoClueStockHandler()

    state_sh.set_successor(nation_sh)
    nation_sh.set_successor(international_sh)
    international_sh.set_successor(no_clue_sh)

    request = {"location": "Vietnam", 
               "type_order": "buy", 
               "stock_acc": my_account,
               "market": apple_market,
               "quantity": quantity}
    
    state_sh.handle(request)
