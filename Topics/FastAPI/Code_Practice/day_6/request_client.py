# requests.py
import requests
from concurrent.futures import ThreadPoolExecutor
import time

URLS = [
    "http://127.0.0.1:8000/sync-sleep?seconds=2",
    "http://127.0.0.1:8000/async-sleep?seconds=2"
]

def fetch(url):
    r = requests.get(url)
    return r.json()

if __name__ == "__main__":
    # Test sync-sleep
    print("=== Testing sync-sleep ===")
    start_sync = time.time()
    for i in range(5):
        fetch(URLS[0])
    duration_sync = time.time() - start_sync
    print(f"Total time for sync-sleep with 5 concurrent requests: {round(duration_sync, 3)} seconds")

    # Test async-sleep
    print("\n=== Testing async-sleep ===")
    start_async = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch, [URLS[1]]*5))
    duration_async = time.time() - start_async
    print(f"Total time for async-sleep with 5 concurrent requests: {round(duration_async, 3)} seconds")
