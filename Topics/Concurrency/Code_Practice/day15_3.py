#Debugging using logging for asyncio as well as debug=True
import asyncio
import logging

logging.basicConfig(level = logging.DEBUG)

async def do_task(i):
    logging.debug(f"Doing task {i}")
    await asyncio.sleep(0.5)
    logging.debug(f"Done task {i}")

async def main():
    tasks = [asyncio.create_task(do_task(i)) for i in range(1,11)]
    await asyncio.gather(*tasks)

asyncio.run(main(), debug=True)
