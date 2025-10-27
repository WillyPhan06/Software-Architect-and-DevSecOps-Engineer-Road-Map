from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fake_db import fake_users_db, create_jwt_token, verify_password, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


app = FastAPI()

@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt_token(user["username"])
    return {"access_token": token, "token_type": "bearer"}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/protected/")
def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": f"Hello {username}, you are authenticated!"}

