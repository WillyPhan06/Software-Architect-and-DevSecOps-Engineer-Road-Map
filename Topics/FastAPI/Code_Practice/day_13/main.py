from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fake_db import fake_users_db
from verify_pw_func import verify_password
from jwt_func import create_jwt_token
from jose import jwt, JWTError
from app_secrets import SECRET_KEY, ALGORITHM

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = fake_users_db.get(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def require_role(required_role: str):
    def role_dependency(current_user: dict = Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return role_dependency

def require_roles(*allowed_roles):
    def role_dependency(current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return role_dependency

@app.get("/dashboard/")
def dashboard(current_user: dict = Depends(require_roles("admin", "user", "man"))):
    return {"message": f"Hello {current_user['username']}, role: {current_user['role']}"}


@app.get("/admin-only/")
def admin_dashboard(current_user: dict = Depends(require_role("admin"))):
    return {"message": f"You are the chosen one lil admin {current_user['username']}"}

@app.get("/user-only/")
def user_dashboard(current_user: dict = Depends(require_role("user"))):
    return {"message": f"WHY DO YOU EVEN EXIST you useless user {current_user['username']}"}



@app.get("/protected/")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}! And wow! You are {current_user['role']}!"}



@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt_token(user["username"], user["role"])
    return {"access_token": token, "token_type": "bearer"}
