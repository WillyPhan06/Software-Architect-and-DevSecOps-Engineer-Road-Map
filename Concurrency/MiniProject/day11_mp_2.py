#Applying multiprocessing with queue to show in order prime numbers the processes found in their own range, and the multiprocessing.Queue() allowed them to communicate very effectively
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor
import os
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def main(start,end):
    multi_queue = multiprocessing.Queue()
    cpu_num = os.cpu_count()
    step = (end-start)//cpu_num
    processes_list = []
    for i in range(cpu_num):
        sub_start = start + i * step
        sub_end = sub_start + step -1 if i < cpu_num - 1 else end
        p = multiprocessing.Process(target=add_prime_num_to_queue, args=(sub_start,sub_end,multi_queue))
        processes_list.append(p)
        p.start()
    flat_prime_list = []
    for _ in processes_list:
        flat_prime_list.extend(multi_queue.get())
    for process in processes_list:
        process.join()


    print(f"There are total of {len(flat_prime_list)} prime numbers")
    print(f"First 10 prime numbers found in order of proccesses are: {flat_prime_list[:10]}")
    print(f"Last 10 prime numbers found in order of processes are: {flat_prime_list[-10:]}")

def add_prime_num_to_queue(start, end, multi_queue):
    sub_prime_list = []
    for i in range(start,end+1):
        if is_prime(i):
            sub_prime_list.append(i)
    multi_queue.put(sub_prime_list)

if __name__ == "__main__":

    start = time.time()
    main(1,100)
    print(f"All took total of {time.time() - start:.2f} seconds")