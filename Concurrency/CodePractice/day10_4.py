#Benchmark CPU task for asyncio for 10k tasks of calculating fibonacci of the number of the nth position in the fibonacci
#Took 13.95 - 14.5 seconds, slightly slower than the threading due to running on single thread
import time
import asyncio

async def fibonacci(n):
    if n <= 2:
        print(1)
        return
    first = 1
    second = 1
    for i in range(2,n):
        third = first + second
        first = second
        second = third
    print(third)

async def main():
    tasks = [asyncio.create_task(fibonacci(i)) for i in range(1,10001)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"All took total of {time.time() - start:.2f} seconds")