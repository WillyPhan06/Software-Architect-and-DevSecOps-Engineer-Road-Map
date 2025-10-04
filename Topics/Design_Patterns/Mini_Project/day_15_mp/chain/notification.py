# chain/notification.py

from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, List
from .stock_acc import StockAccount

@dataclass
class NotificationCenter:
    accounts: List[StockAccount] = field(default_factory=list)

    def add_acc_for_notify(self, stock_acc: StockAccount):
        self.accounts.append(stock_acc)   

    def notify(self, message: str):
        for account in self.accounts:
            account.receive_notification(message) 