#Benchmark of threading in I/O bound tasks, ran in around 5 seconds with a little bit 0.01 - 0.02 secs overhead sometimes
import threading, time
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

def do_something_delay(i):
    with lock:
        print(f"Doing delay task {i}")
    time.sleep(5)
    with lock:
        print(f"Done doing delay task {i}")

start = time.time()
task_order_list = [i for i in range(1,11)]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(do_something_delay,task_order_list)
print(f"All done in total of {time.time() - start:.2f} seconds")