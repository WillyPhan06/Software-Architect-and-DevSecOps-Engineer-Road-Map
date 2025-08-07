#Well this is for opening file using both asyncio and threading, since asyncio can't really open file without blocking so we have threading here
import asyncio
import time

file_name = r"C:\Users\ADMIN\Downloads\ohmylord.txt"


def open_and_read_file(file, i):
    print(f"Task {i} opening file: {file}")
    with open(file, "r", encoding="utf-8") as opened_file:
        print(f"Task {i} returning read results from file: {file}")
        return opened_file.read()


async def converting_to_thread(file, i):
    content = await asyncio.to_thread(open_and_read_file, file, i)
    print(f"Printing content for task {i}:")
    print(content)


async def main(file):
    print(f"Creating list of coroutine objects ready to run")
    tasks = [asyncio.create_task(converting_to_thread(file, i)) for i in range(1, 11)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main(file_name))
print(f"All took total of {time.time() - start:.2f} seconds")