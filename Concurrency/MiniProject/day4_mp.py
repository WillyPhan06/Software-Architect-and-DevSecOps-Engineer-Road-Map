#Downloading web via threads, speed up to 0.6 secs, in average is from 1 sec to below.
import requests
import time
import threading

def download_web(i):
    print(f"Start downloading via thread {i}")
    response = requests.get("https://example.com/")
    print(f"Finished downloading {len(response.content)} bytes of web via thread {i}")

threads = []

start = time.time()
for i in range(10):
    t = threading.Thread(target=download_web, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(f"All finished in {time.time() - start:.2f} seconds")

