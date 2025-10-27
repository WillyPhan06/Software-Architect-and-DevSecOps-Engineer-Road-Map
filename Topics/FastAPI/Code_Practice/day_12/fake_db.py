import bcrypt
from datetime import datetime, timedelta, timezone
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
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"sub": username, "exp": int(expire.timestamp())}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password)