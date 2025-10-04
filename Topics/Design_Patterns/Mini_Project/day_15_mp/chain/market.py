#chain/market.py

from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, List

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