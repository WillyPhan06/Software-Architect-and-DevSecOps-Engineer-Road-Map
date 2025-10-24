from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


SECRET_KEY = "supersecretjwtkey"
ALGORITHM = "HS256"

def create_jwt_token(user_id: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    payload = {"sub": user_id, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

app = FastAPI()

@app.post("/token/")
def login(user_id: str):
    token = create_jwt_token(user_id)
    return {"access_token": token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/jwt-protected/")
def jwt_protected(token: str = Depends(oauth2_scheme)):
    user = decode_jwt_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": user, "message": "Access granted"}



@app.post("/oauth-token/")
def oauth_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # For demo, no real DB check
    if form_data.username != "alice" or form_data.password != "password":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt_token(form_data.username)
    return {"access_token": token, "token_type": "bearer"}
