#Applying gather all coded from scratch and with random to simulate random intervals, the longest time this will hit will be the longest time of b each time we run
import asyncio
import random
import time

list_of_tuples = []

for i in range(5):
    list_of_tuples.append(tuple([random.randint(1,5),random.randint(1,5)]))


async def do_delay_stuff(a,b):
    print(f"Start doing task {a} with I/O time of {b} seconds")
    await asyncio.sleep(b)
    print(f"Finished doing task {a} with I/O time of {b} seconds")

async def main():
    global list_of_tuples
    tasks = []
    for tuple in list_of_tuples:
        tasks.append(do_delay_stuff(*tuple))
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"All took total of {time.time() - start:.2f} seconds")