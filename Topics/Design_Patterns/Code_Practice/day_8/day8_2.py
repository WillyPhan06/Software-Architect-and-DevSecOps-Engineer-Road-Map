# Instantiate and update code and play around with dynamic facades, very flexible and overwriting the last step getatr to delegate to appropriate subsystem

class Inventory:
    def check_stock(self, item_id): return True

class Payment:
    def charge(self, amount): return f"paid {amount} USD"

class Shipping:
    def ship(self, item_id): return "shipped"

class Notification:
    def notify(self, user, message): print(f"Notify {user}: {message}")

class DynamicFacade:
    def __init__(self, **components):
        self._components = components

    def __getattr__(self, item):
        # Delegate to appropriate subsystem
        if item in self._components:
            return self._components[item]
        raise AttributeError(f"No component named {item}")

# Usage
facade = DynamicFacade(payment=Payment(), inventory=Inventory())
print(facade.payment.charge(50))

