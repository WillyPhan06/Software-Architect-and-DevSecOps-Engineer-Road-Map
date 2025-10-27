import bcrypt

password = b"mysecret"  # must be bytes
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Hashed:", hashed)

# Verify
print(bcrypt.checkpw(b"mysecret", hashed))  # True
print(bcrypt.checkpw(b"wrongpass", hashed)) # False

from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "supersecretjwtkey"
ALGORITHM = "HS256"

fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": bcrypt.hashpw(b"password123", bcrypt.gensalt())
    },
    "bob": {
        "username": "bob",
        "hashed_password": bcrypt.hashpw(b"secret456", bcrypt.gensalt())
    }
}

def create_jwt_token(username: str, expires_delta: timedelta = timedelta(minutes=30)):
    expire = datetime.now(datetime.timezone.utc) + expires_delta
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
