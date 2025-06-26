#Benchmark of multiprocessing in I/O bound tasks, ran in around 6 seconds. As expected its inefficient since it wastes resource making new processes for waiting bound tasks
import time
from concurrent.futures import ProcessPoolExecutor

def do_something_delay(i):
    print(f"Task {i} start something delay")
    time.sleep(5)
    print(f"Task {i} done delaying")

if __name__ == "__main__":
    start = time.time()
    tasks = [i for i in range(1,11)]
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(do_something_delay,tasks)
    print(f"All took total of {time.time() - start:.2f} seconds")

