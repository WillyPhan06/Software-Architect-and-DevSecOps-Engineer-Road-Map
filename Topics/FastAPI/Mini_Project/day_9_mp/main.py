from models.user import User

# Create 3 users
alice = User("Alice", 100)
bob = User("Bob", 50)
carol = User("Carol", 25)

# Alice sends 30 to Bob
block1 = alice.create_block(bob, 30)
alice.send_block_to_pool(block1)

# Bob sends 10 to Carol
block2 = bob.create_block(carol, 10)
bob.send_block_to_pool(block2)

# Carol sends 5 to Alice
block3 = carol.create_block(alice, 5)
carol.send_block_to_pool(block3)

# Each user verifies transactions in their pool
for user in [alice, bob, carol]:
    user.verify_block_in_pool()

# Print final balances
for user in [alice, bob, carol]:
    print(user)

# Print ledgers
for user in [alice, bob, carol]:
    print(f"{user.name}'s ledger: {user.ledger}")
