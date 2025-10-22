import uuid
from typing import List
from .block import Block
from .seed_user import SeedUser

class User:
    def __init__(self, name: str, balance: float, ledger: List[Block] = None, pool: List[Block] = None):
        self.id: str = str(uuid.uuid4())
        self.name = name
        self.balance = balance
        self.ledger = ledger or []
        self.pool = pool or []
        SeedUser.users.append(self)
        print(f"User created: {self.name} | id: {self.id} | Balance: {self.balance}")

    def check_balance(self, amount: float) -> bool:
        return self.balance >= amount

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float) -> bool:
        if self.check_balance(amount):
            self.balance -= amount
            return True
        return False

    def create_block(self, receiver: 'User', amount: float) -> Block:
        return Block(sender=self, receiver=receiver, amount=amount)

    def add_block_to_ledger(self, block: Block):
        self.ledger.append(block)

    def add_block_to_pool(self, block: Block):
        self.pool.append(block)

    def send_block_to_pool(self, block: Block):
        for user in SeedUser.users:
            user.add_block_to_pool(block)

    def verify_block_in_pool(self):
        # Verify each block in pool
        for block in self.pool:
            if block.sender.check_balance(block.amount):
                print(f"{self.name} verified block: {block}")
                self.add_block_to_ledger(block)
                if block.sender == self:
                    block.sender.decrease_balance(block.amount)
                    block.receiver.increase_balance(block.amount)
                    print(f"{self.name}'s Self Transaction Successful: {block}")
        self.pool.clear()

    def __repr__(self):
        return f"User({self.name}, Balance: {self.balance})"
