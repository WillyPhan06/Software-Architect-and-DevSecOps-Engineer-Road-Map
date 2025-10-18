# main.py
from fastapi import FastAPI
import time, asyncio
from starlette.concurrency import run_in_threadpool
import httpx

app = FastAPI()

def blocking_heavy_task(x: int):
    time.sleep(2)   # simulates blocking I/O or CPU-bound sync work
    return {"result": x * 2}

@app.get("/proxy-async")
async def proxy_async(url: str = "https://httpbin.org/delay/1"):
    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=10.0)
    return {"status": r.status_code, "len": len(r.text)}

@app.get("/sync-call-in-async")
async def sync_call_in_async(x: int = 10):
    # BAD: calling blocking_heavy_task directly would block event loop
    result = await run_in_threadpool(blocking_heavy_task, x)
    return {"from_threadpool": result}


@app.get("/sync-sleep")
def sync_sleep(seconds: int = 2):
    start = time.time()                  # start timer
    time.sleep(seconds)                  # BLOCKING: stops the worker thread
    duration = time.time() - start       # calculate elapsed time
    return {
        "endpoint": "sync-sleep",
        "slept": seconds,
        "duration_seconds": round(duration, 3)  # return measured time
    }

@app.get("/async-sleep")
async def async_sleep(seconds: int = 2):
    start = time.time()                  # start timer
    await asyncio.sleep(seconds)         # NON-BLOCKING: yields to event loop
    duration = time.time() - start       # calculate elapsed time
    return {
        "endpoint": "async-sleep",
        "slept": seconds,
        "duration_seconds": round(duration, 3)  # return measured time
    }
