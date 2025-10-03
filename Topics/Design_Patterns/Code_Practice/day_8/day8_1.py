# Instantiate the classes and use the facade to process an order
# facade/order_facade.py
class Inventory:
    def check_stock(self, item_id): return True

class Payment:
    def charge(self, amount): return "paid"

class Shipping:
    def ship(self, item_id): return "shipped"

class Notification:
    def notify(self, user, message): print(f"Notify {user}: {message}")

class OrderFacade:
    def __init__(self):
        self.inv = Inventory()
        self.pay = Payment()
        self.ship = Shipping()
        self.notif = Notification()

    def process_order(self, user: str, item_id: str, amount: float):
        if not self.inv.check_stock(item_id):
            raise ValueError("Out of stock")
        status = self.pay.charge(amount)
        if status != "paid":
            raise RuntimeError("Payment failed")
        ship_status = self.ship.ship(item_id)
        self.notif.notify(user, f"Order {item_id} processed: {ship_status}")
        return ship_status
    
# Client code
if __name__ == "__main__":
    facade = OrderFacade()
    facade.process_order("Alice", "item123", 100.0)
