from fastapi import FastAPI, HTTPException, Query
from contextlib import asynccontextmanager
import csv
import time

LOG_FILE = "log.txt"

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_time = time.time()
    start_ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    print(f"Starting up at {start_ts}")
    
    # Log startup
    with open(LOG_FILE, "a") as f:
        f.write(f"Start: {start_ts}\n")
    
    # Load CSV into memory for queries
    app.state.data = []
    with open("data.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert private column to boolean
            row["private"] = row["private"] == "True"
            app.state.data.append(row)
    
    yield  # <-- Server now starts handling requests
    
    # Shutdown logic
    end_time = time.time()
    end_ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
    duration = end_time - start_time
    print(f"Shutting down at {end_ts}, duration: {duration:.2f} seconds")
    
    # Log shutdown and duration
    with open(LOG_FILE, "a") as f:
        f.write(f"Shutdown: {end_ts}\n")
        f.write(f"Duration: {duration:.2f} seconds\n\n")

app = FastAPI(lifespan=lifespan)

@app.get("/users/")
async def get_users(query: str = Query(default="", description="Filter by name substring")):
    result = []
    for row in app.state.data:
        if row["private"]:
            continue  # Skip private rows
        if query.lower() in row["name"].lower():
            result.append({"id": row["id"], "name": row["name"]})
    if not result:
        raise HTTPException(status_code=404, detail="No matching users found")
    return result
