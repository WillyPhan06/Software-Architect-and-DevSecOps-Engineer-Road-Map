import bcrypt

password = b"mysecret"  # must be bytes
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Hashed:", hashed)

# Verify
print(bcrypt.checkpw(b"mysecret", hashed))  # True
print(bcrypt.checkpw(b"wrongpass", hashed)) # False



