from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()
API_KEY = "supersecretapikey"
api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return api_key

@app.get("/protected/")
def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "Access granted"}
