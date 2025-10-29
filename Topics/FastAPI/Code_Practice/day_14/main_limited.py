from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

origins = [
        "http://localhost",
        "http://localhost:3000",
        "https://myfrontend.com",
        "http://localhost:5500"
    ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # domains allowed
        allow_credentials=True,
        allow_methods=["*"],    # GET, POST, etc.
        allow_headers=["*"],    # custom headers
    )

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

@app.get("/limited/")
@limiter.limit("5/minute")
def limited_endpoint(request: Request):
    return {"message": "This endpoint is rate-limited"}
