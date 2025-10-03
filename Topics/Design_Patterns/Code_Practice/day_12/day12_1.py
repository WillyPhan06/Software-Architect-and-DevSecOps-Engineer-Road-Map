# This state pattern design now use enum and auto to assign different states as well as using a dictionary to coordinate them through trigger method of the vending machine class

from enum import Enum, auto

class S(Enum):
    NO_COIN = auto()
    HAS_COIN = auto()
    DISPENSING = auto()
    SOLD_OUT = auto()

# events: 'insert_coin', 'select_item', 'dispense', 'restock'
# transitions[(state, event)] = (next_state, action_fn)
def action_insert(ctx, amount):
    ctx.balance += amount
    print(f"Performed insert action of {amount} making the balance become {ctx.balance}")
    return None

def action_select(ctx, code):
    item = ctx.inventory.get(code)
    if not item or item["stock"] <= 0:
        print("Invalid / out of stock")
        return None
    ctx.selected = code
    if ctx.balance >= item["price"]:
        return ("dispense",)
    else:
        return None

# Build transitions dict (abbreviated)
TRANSITIONS = {
    (S.NO_COIN, 'action_insert'): (S.NO_COIN, action_insert),
    (S.HAS_COIN, 'select_item'): (S.DISPENSING, lambda ctx, code: ctx.dispense()),
    # etc...
}

# Simple runner:
class TableVending:
    def __init__(self, inventory):
        self.state = S.NO_COIN
        self.inventory = inventory
        self.balance = 0
    def trigger(self, event, *args):
        key = (self.state, event)
        if key not in TRANSITIONS:
            print("Event ignored")
            return
        next_state, action = TRANSITIONS[key]
        if action:
            action(self, *args)
        self.state = next_state

if __name__ == "__main__":
    inv = {"A1": {"price": 100, "stock": 1}, "B2": {"price": 50, "stock": 2}}
    table_vending = TableVending(inventory=inv)
    table_vending.trigger("action_insert",50)
    

