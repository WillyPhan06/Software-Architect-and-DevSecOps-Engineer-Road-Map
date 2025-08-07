#Exampe of applying thread pool executor into very simple task, its for today's topic
import time
from concurrent.futures import ThreadPoolExecutor

def do_delay_stuff(i):
    print(f"Task {i} starting to sleep for {i} seconds")
    time.sleep(i)
    print(f"Task {i} finished sleeping for {i} seconds")

start = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(1,6):
        executor.submit(do_delay_stuff,i)

print(f"All took total of {time.time() - start:.2f} seconds")