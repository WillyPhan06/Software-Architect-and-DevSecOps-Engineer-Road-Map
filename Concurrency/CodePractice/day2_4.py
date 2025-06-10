#Creating threads using for loop
import threading
import time


def waiting(a):
    print(f"Yeah i'm doing task {a} in 2 seconds")
    time.sleep(2)
    print(f"Yo i did the task {a}")

threads = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=waiting, args=(i,))
    threads.append(t)
    t.start()

for i in threads:
    i.join()

print(f"All done in {time.time() - start:.2f} seconds")