#Understanding and Playing around with the Decorator Pattern

# classic_decorator.py
from abc import ABC, abstractmethod

# Component interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Concrete component
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Email: {message}")

# Base decorator
class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str):
        self._wrapped.send(message)

# Concrete decorators
class SMSDecorator(NotifierDecorator):
    def send(self, message: str):
        print(f"SMS: {message}")
        super().send(message)

class SlackDecorator(NotifierDecorator):
    def send(self, message: str):
        print(f"Slack: {message}")
        super().send(message)

if __name__ == "__main__":
    notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
    notifier.send("Server down!")
    print("Fixing issue...")
    up_notifier = SMSDecorator(SlackDecorator(EmailNotifier()))
    up_notifier.send("Server up!")
