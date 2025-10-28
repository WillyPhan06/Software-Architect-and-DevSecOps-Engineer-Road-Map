from datetime import datetime, timezone, timedelta
from jose import jwt
from app_secrets import SECRET_KEY, ALGORITHM


def create_jwt_token(username: str, role: str, expires_delta: timedelta = timedelta(minutes=30)):
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"sub": username, "role": role, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
