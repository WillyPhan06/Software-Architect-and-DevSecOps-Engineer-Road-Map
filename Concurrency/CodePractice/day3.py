#Threading with lock for hard computing
import threading
import time

counter = 0
locking = threading.Lock()

def update_global(task_name):
    global counter
    print(f"Task {task_name} starting incrementing")
    with locking:
        for _ in range(1000000):
            counter += 1
    print(f"Task {task_name} finished incrementing")



threads = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=update_global, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(f"Total time took is {time.time() - start:.2f} seconds")
print(counter)

