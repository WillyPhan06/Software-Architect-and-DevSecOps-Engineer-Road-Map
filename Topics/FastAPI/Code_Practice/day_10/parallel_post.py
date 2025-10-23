import asyncio
import httpx

async def send_post(name):
    async with httpx.AsyncClient() as client:
        r = await client.post("http://127.0.0.1:8000/async-job/", params={"job_name": name})
        print(r.json())

async def main():
    tasks = [send_post(f"job{i}") for i in range(5)]  # 10 parallel POSTs
    await asyncio.gather(*tasks)

asyncio.run(main())
