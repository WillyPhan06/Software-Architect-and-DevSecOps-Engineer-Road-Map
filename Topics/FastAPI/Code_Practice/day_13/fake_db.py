import bcrypt

fake_users_db = {
    "alice": {"username": "alice", "hashed_password": bcrypt.hashpw(b"password123", bcrypt.gensalt()), "role": "user"},
    "bob": {"username": "bob", "hashed_password": bcrypt.hashpw(b"secret456", bcrypt.gensalt()), "role": "admin"},
    "charlie": {"username": "charlie", "hashed_password": bcrypt.hashpw(b"hehe123", bcrypt.gensalt()), "role": "man"}
}
