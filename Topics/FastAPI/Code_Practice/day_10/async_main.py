import asyncio
from fastapi import FastAPI, BackgroundTasks
import time


app = FastAPI()

async def async_task(name: str, start: float):
    await asyncio.sleep(2)
    timeline = time.time() - start
    print(f"Task done: {name} in timeline of {timeline:.2f} seconds")

async def do_background(job_name: str, start: float):
    tasks = [async_task(job_name + str(i), start) for i in range(3)]
    await asyncio.gather(*tasks)

@app.post("/async-job/")
async def async_job(background_task: BackgroundTasks, job_name: str):
    start = time.time()
    background_task.add_task(do_background, job_name, start)
    return {"message": f"Job {job_name} completed in {time.time() - start:.2f} seconds"}

@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    # Simulate DB connection or cache initialization
    app.state.db = {"connected": True}

