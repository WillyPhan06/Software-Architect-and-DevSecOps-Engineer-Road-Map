#Another example using try except and catch asyncio.CancelledError by manually cancel it with task.cancel()
import asyncio
import time

async def doing_long_task():
    print("Start doing long task")
    await asyncio.sleep(5)
    print("Done doing long task")

async def main():
    print("Creating doing long task")
    do_long_task = asyncio.create_task(doing_long_task())
    await asyncio.sleep(2)
    do_long_task.cancel()
    try:
        await do_long_task
    except asyncio.CancelledError:
        print("Task got cancelled")

asyncio.run(main())