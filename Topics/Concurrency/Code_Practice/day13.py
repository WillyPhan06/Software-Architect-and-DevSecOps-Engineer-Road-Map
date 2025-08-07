#Practicing with asyncio.wait_for(function, timeout=s)
import asyncio
import random

async def do_delay_task(i):
    global count
    print(f"Task {i} starting task")
    await asyncio.sleep(i)
    print(f"Task {i} done sleeping")
    count += 1

async def arrange_do_task(tasks):
    async_tasks = [asyncio.create_task(do_delay_task(task)) for task in tasks]
    print("Finished arranged async tasks into list")
    print("Starting to execute async tasks")
    await asyncio.gather(*async_tasks)

async def main():
    tasks = [i for i in range(1,11)]
    try:
        random_num = random.randint(1,10)
        print(f"Decided random number to be {random_num}")
        await asyncio.wait_for(arrange_do_task(tasks), timeout=random_num)
    except asyncio.TimeoutError:
        print(f"Failed at task {count+1} due to TimeoutError")

count = 0
asyncio.run(main())