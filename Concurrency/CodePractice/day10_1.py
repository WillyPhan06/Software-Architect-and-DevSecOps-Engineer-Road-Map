#Benchmark of asyncio in I/O bound tasks, ran in around 5 seconds with also little bit 0.01 - 0.02 secs, definitely expected for I/O tasks for both asyncio and threads
import asyncio, time

async def do_something_delay(i):
    print(f"Task {i} start something delay")
    await asyncio.sleep(5)
    print(f"Task {i} done delaying")

async def main():
    tasks = [asyncio.create_task(do_something_delay(i)) for i in range(1,11)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"All took total of {time.time() - start:.2f} seconds")