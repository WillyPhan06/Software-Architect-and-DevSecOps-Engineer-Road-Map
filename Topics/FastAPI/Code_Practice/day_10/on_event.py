from fastapi import FastAPI, BackgroundTasks
from contextlib import asynccontextmanager
import time

start = time.time()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting up at {time.time() - start:.2f} seconds")
    # Simulate DB connection or cache initialization
    app.state.db = {"connected": True}
    yield
    print(f"Shutting down at {time.time() - start:.2f} seconds")
    # Simulate DB disconnection or cleanup
    app.state.db = {"connected": False}

app = FastAPI(lifespan=lifespan)

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(f"{message} at {time.time()-start} second\n")

@app.get("/")
async def root():
    return {"message": "Hello, world!", "db_connected": app.state.db["connected"]}

@app.get("/check-db")
async def check_db(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Checked DB connection status at {time.time() - start:.2f} seconds")
    return {"db_status": app.state.db["connected"]}
