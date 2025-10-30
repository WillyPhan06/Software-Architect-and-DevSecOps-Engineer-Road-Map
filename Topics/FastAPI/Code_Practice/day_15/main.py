from fastapi import FastAPI, Request, HTTPException, Query, Header
from fastapi.responses import RedirectResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/auth/google/callback"

@app.get("/auth/google")
def google_login():
    url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={CLIENT_ID}&response_type=code&"
        f"scope=openid%20email%20profile&"
        f"redirect_uri={REDIRECT_URI}"
    )
    return RedirectResponse(url)

@app.get("/auth/google/callback")
def google_callback(code: str):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    resp = httpx.post(token_url, data=data)
    token_data = resp.json()
    access_token = token_data.get("access_token")
    return {"access_token": access_token}

@app.get("/avatar")
def get_avatar(token: str = Query(..., description="Google OAuth2 access token")):
    """
    Returns the user's Google profile picture URL.
    """
    headers = {"Authorization": f"Bearer {token}"}
    resp = httpx.get("https://www.googleapis.com/oauth2/v1/userinfo", headers=headers)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()
    avatar_url = data.get("picture")
    if not avatar_url:
        raise HTTPException(status_code=404, detail="No avatar found")

    return {"avatar_url": avatar_url}

@app.get("/avatar_pro")
def get_avatar(authorization: str = Header(..., description="Authorization header with Bearer token")):
    """
    Returns the user's Google profile picture URL.
    Expects Authorization: Bearer ACCESS_TOKEN
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization[len("Bearer "):]
    headers = {"Authorization": f"Bearer {token}"}

    resp = httpx.get("https://www.googleapis.com/oauth2/v1/userinfo", headers=headers)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()
    avatar_url = data.get("picture")
    if not avatar_url:
        raise HTTPException(status_code=404, detail="No avatar found")

    return {"avatar_url": avatar_url}

