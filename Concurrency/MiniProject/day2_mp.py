#Applied threading to simulate downloading, instead of taking total of 15 secs, this took 5 secs thanks to the power of concurrency.
import threading
import time

def downloading(name):
    print(f"Currently downloading file {name}")
    time.sleep(name)
    print(f"Finished downloading file {name}")


file_list = [1,2,3,4,5]
thread_list = []
start = time.time()
for file in file_list:
    t = threading.Thread(target=downloading, args=(file,))
    thread_list.append(t)
    t.start()

for thread in thread_list:
    thread.join()

print(f"Total time taken is {time.time() - start:.2f} seconds")
