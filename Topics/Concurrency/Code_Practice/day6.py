#Example of manual threading in downloading websites, not for today's topic tho cause we will use thread pool executor
import threading
import time
import requests

url_list = ["https://example.com/", "https://httpbin.org/html", "https://httpbin.org/get", "https://www.wikipedia.org/", "https://www.google.com/robots.txt"]
thread_list = []
task_order = 0

def downloading(url, i):
    print(f"Task {i} starting downloading url: {url}")
    task_start = time.time()
    response = requests.get(url)
    print(f"Task {i} finished downloading {len(response.content)} bytes of content from url: {url} with time taken: {time.time() - task_start:.2f} seconds")

start = time.time()

for url in url_list:
    task_order += 1
    t = threading.Thread(target=downloading, args=(url,task_order))
    thread_list.append(t)
    t.start()

for thread in thread_list:
    thread.join()

print(f"All took total of {time.time() - start:.2f} seconds")