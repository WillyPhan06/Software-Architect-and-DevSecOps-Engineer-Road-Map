#Combined both async and threading to download the web and get number of bytes using async then write it to file using threading
import asyncio
import time
import aiohttp
from pathlib import Path

output_file = Path(r"C:\Users\ADMIN\Downloads\ohmylord.txt")

url_example = "https://example.com/"

async def get_bytes_from_url(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            bytes_num = len(data)
            print(f"Task {i} downloaded {bytes_num} bytes from url: {url}")
            await asyncio.to_thread(write_to_file,bytes_num,url,i)

def write_to_file(bytes_num, url, i):
    with open(output_file, "a", encoding="utf-8") as file:
        file.write(f"Task {i} downloaded {bytes_num} bytes from url: {url}")
    print(f"Task {i} logged into output file")

async def main():
    tasks = [asyncio.create_task(get_bytes_from_url(url_example,i)) for i in range(1,11)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"All took total of {time.time() - start:.2f} seconds")