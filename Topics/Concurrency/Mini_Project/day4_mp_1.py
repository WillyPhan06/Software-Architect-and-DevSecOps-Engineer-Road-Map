#Downloading web via async, based on theory should be faster but due to aiohttp overhead, its in average 1.1 - 1.2 secs
import aiohttp
import asyncio
import time


async def downloading(session, i):
    async with session.get("https://example.com/") as response:
        content = await response.read()
        print(f"Task {i} finished downloading {len(content)} bytes")

async def create_session():
    async with aiohttp.ClientSession() as session:
        tasks = [downloading(session, i) for i in range(10)]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(create_session())
print(f"All took {time.time() - start:.2f} seconds")
