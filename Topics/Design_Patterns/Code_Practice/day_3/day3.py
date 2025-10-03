#Following tutorial and code from memory with error fixes when applying Factory Method Pattern to replace bad if else structure

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float, currency: str) -> str:
        pass

@dataclass
class PayPalProcessor(PaymentProcessor):
    email: str

    def pay(self, amount: float, currency: str) -> str:
        return f"Processed payment of {amount} {currency} via PayPal for {self.email}"
    
@dataclass
class StripeProcessor(PaymentProcessor):
    api_key: str

    def pay(self, amount: float, currency: str) -> str:
        return f"Processed payment of {amount} {currency} via Stripe with API key {self.api_key}"
    

class PaymentFactory:
    _registry = {}
    @classmethod
    def register_processor(cls, name: str, processor_cls: type[PaymentProcessor]):
        cls._registry[name] = processor_cls
        print("Registered processor:", name)


def register_all():
    PaymentFactory.register_processor("paypal", PayPalProcessor)
    PaymentFactory.register_processor("stripe", StripeProcessor)

register_all()