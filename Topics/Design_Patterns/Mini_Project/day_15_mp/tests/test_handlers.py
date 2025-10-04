from chain.transaction_center import TransactionCenter
from chain.notification import NotificationCenter
from chain.stock_acc import StockAccount
from chain.market import AppleMarket
from chain.handlers import StockHandler, StateStockHandler, NationalStockHandler, InternationalStockHandler, NoClueStockHandler

def test_state_handler():
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

    request = {"location": "San Francisco", 
               "type_order": "buy", 
               "stock_acc": my_account,
               "market": apple_market,
               "quantity": quantity}
    
    result = state_sh.handle(request)
    assert result == "State_Success"

def test_national_handler():
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

    request = {"location": "California", 
               "type_order": "buy", 
               "stock_acc": my_account,
               "market": apple_market,
               "quantity": quantity}
    
    result = state_sh.handle(request)
    assert result == "National_Success"

def test_international_handler():
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

    request = {"location": "China", 
               "type_order": "buy", 
               "stock_acc": my_account,
               "market": apple_market,
               "quantity": quantity}
    
    result = state_sh.handle(request)
    assert result == "International_Success"

def test_no_clue_handler():
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

    request = {"location": "Nowhere", 
               "type_order": "buy", 
               "stock_acc": my_account,
               "market": apple_market,
               "quantity": quantity}
    
    result = state_sh.handle(request)
    assert result == "NoClue_Success"

