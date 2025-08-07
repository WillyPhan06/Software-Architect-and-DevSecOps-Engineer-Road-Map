#Applying ThreadPoolExecutor to download many web concurrently efficiently, good spot here is applying enumerate when organizing tasks in order.
import time
import requests
from concurrent.futures import ThreadPoolExecutor

url_list = ["https://example.com/", "https://httpbin.org/html", "https://httpbin.org/get", "https://www.wikipedia.org/", "https://www.google.com/robots.txt"]

task_order = 0

def downloading(url, i):
    print(f"Task {i} starting downloading url: {url}")
    task_start = time.time()
    response = requests.get(url)
    print(f"Task {i} finished downloading {len(response.content)} bytes of content from url: {url} with time taken: {time.time() - task_start:.2f} seconds")

start = time.time()

with ThreadPoolExecutor(max_workers=len(url_list)) as executor:
    for i, url in enumerate(url_list,1):
        executor.submit(downloading, url, i)


print(f"All took total of {time.time() - start:.2f} seconds")