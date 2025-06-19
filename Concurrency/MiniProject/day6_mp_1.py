#Applying .map() instead of submit for iterable which is super efficient and clean
from concurrent.futures import ThreadPoolExecutor
import time
import requests

url_list = ["https://example.com/", "https://httpbin.org/html", "https://httpbin.org/get", "https://www.wikipedia.org/", "https://www.google.com/robots.txt"]


def downloading(url):
    print(f"Start downloading url: {url}")
    task_start = time.time()
    response = requests.get(url)
    print(f"Finished downloading {len(response.content)} bytes of content from url: {url} in {time.time() - task_start:.2f} seconds")

start = time.time()

with ThreadPoolExecutor(max_workers=len(url_list)) as executor:
    executor.map(downloading, url_list)

print(f"All took total of {time.time() - start:.2f} seconds")