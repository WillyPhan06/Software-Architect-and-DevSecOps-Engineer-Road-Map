#Simulating fetching APIs with different time limit and time done for each one and return list of status of suceeded and failed tasks simulating fetching API
import asyncio
import random

lock = asyncio.Lock()


async def do_delay_task(i, limit):
    global stat_nested_list
    random_num = random.randint(1, 10)
    print(f"Task {i} fetching API expecting to get in {random_num} seconds")
    if random_num >= limit:
        async with lock:
            stat_nested_list.append([i,limit,random_num,"Failed"])
    await asyncio.sleep(random_num)
    print(f"Task {i} successfully fetched API in {random_num} seconds")
    async with lock:
        stat_nested_list.append([i,limit,random_num,"Succeed"])



async def arrange_task(i):
    random_delay = random.randint(1,10)
    print(f"Task {i} got limit of {random_delay} to fetch before timeout")
    arranged_task = asyncio.create_task(do_delay_task(i, random_delay))
    await asyncio.sleep(random_delay)
    arranged_task.cancel()
    try:
        await arranged_task
    except asyncio.CancelledError:
        print(f"Task {i} failed fetching API in time limit of {random_delay} seconds")


async def main():
    tasks = [i for i in range(1,11)]
    running_tasks = [asyncio.create_task(arrange_task(task)) for task in tasks]
    await asyncio.gather(*running_tasks)
    for status in stat_nested_list:
        i, limit, random_num, stat = status
        print(f"Task {i} got limit of {limit} seconds and done in {random_num} seconds. Result: {stat}")

stat_nested_list = []

asyncio.run(main())