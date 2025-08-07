#Great example of practicing producer consumer pattern applying threading and queue which makes both runs in parallel resulting in run time of longest wait time of a task instead of sum
import threading
import queue
import time
import random

lock = threading.Lock()

buffer = queue.Queue(maxsize=100)
sum_sleep = 0
longest_sleep = 0
thread_order_list = [i for i in range(1,11)]
producer_thread_list = []
consumer_thread_list = []

def producer_task(i):
    global sum_sleep, longest_sleep
    item = random.randint(1,100)
    print(f"Producer Task {i} created item {item}")
    buffer.put(item)
    print(f"Producer Task {i} put item {item} into the buffer")
    sleep_time = random.uniform(0.1,1)
    with lock:
        if sleep_time > longest_sleep:
            longest_sleep = sleep_time
        sum_sleep += sleep_time
    time.sleep(sleep_time)
    print(f"Producer Task {i} slept for {sleep_time:.2f} seconds")

def consumer_task(i):
    global sum_sleep, longest_sleep
    item = buffer.get()
    print(f"Consumer Task {i} got item {item} from buffer")
    print(f"Consumer Task {i} with item {item} checked done")
    sleep_time = random.uniform(0.1, 1)
    with lock:
        if sleep_time > longest_sleep:
            longest_sleep = sleep_time
        sum_sleep += sleep_time
    time.sleep(sleep_time)
    print(f"Consumer Task {i} slept for {sleep_time:.2f} seconds")
start = time.time()

for i in range(1, 11):
    producer_thread = threading.Thread(target=producer_task, args=(i,))
    consumer_thread = threading.Thread(target=consumer_task, args=(i,))
    producer_thread_list.append(producer_thread)
    consumer_thread_list.append(consumer_thread)
    producer_thread.start()
    consumer_thread.start()

for i in range(10):
    producer_thread_list[i].join()
    consumer_thread_list[i].join()

print(f"All took total of {time.time() - start:.2f} seconds")
print(f"Total sum of sleep was {sum_sleep:.2f} seconds")
print(f"Longest sleep time was {longest_sleep:.2f} seconds")
