# main.py

if __name__ == "__main__":
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi import FastAPI

    app = FastAPI()

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

    @app.get("/hello")
    def hello():
        return {"message": "CORS is working!"}

