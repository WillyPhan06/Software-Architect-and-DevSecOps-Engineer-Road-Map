import asyncio
import httpx
import time

URL = "http://127.0.0.1:8000/proxy-async"

async def fetch(i, client, url):
    global start
    r = await client.get(url)
    duration_fetch = time.time() - start
    print(f"Request {i+1} completed in timeline of {round(duration_fetch, 2)} seconds")
    return r.json()

async def main():
    async with httpx.AsyncClient(timeout=15.0) as client:
        tasks = [fetch(i, client, URL) for i in range(5)]  # fire 5 requests
        results = await asyncio.gather(*tasks)
        for i, res in enumerate(results):
            print(f"Request {i+1}:", res)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print("Total elapsed time:", round(time.time() - start, 2), "seconds")
