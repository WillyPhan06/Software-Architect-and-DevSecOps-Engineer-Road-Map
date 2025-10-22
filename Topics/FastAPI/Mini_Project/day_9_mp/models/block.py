# block.py
import uuid

class Block:
    def __init__(self, sender: 'User', receiver: 'User', amount: float):
        self.id: str = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"Block({self.sender.name} -> {self.receiver.name}, {self.amount})"
