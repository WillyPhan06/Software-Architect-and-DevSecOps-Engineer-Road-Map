#Practice added debug=True for asyncio to show first red debug line but later in further runs i don't see it again due to avoiding flood to the console
import asyncio

async def do_work(i):
    print(f"Task {i} doing work")
    await asyncio.sleep(0.5)
    print(f"Task {i} done working")

async def main():
    tasks = [asyncio.create_task(do_work(i)) for i in range(1,11)]
    await asyncio.gather(*tasks)

asyncio.run(main(), debug=True)