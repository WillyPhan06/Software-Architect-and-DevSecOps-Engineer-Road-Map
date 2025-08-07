#Applying ProcessPoolExecutor to run calculate number of prime numbers, tweak from using Queue to not using queue by own scratch code and idea
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
    cpu_num = os.cpu_count()
    step = (end-start)//cpu_num

    sub_start_end_list = []
    for i in range(cpu_num):
        sub_start = start + i * step
        sub_end = sub_start + step -1 if i < cpu_num - 1 else end
        sub_start_end_list.append((sub_start,sub_end))
    with ProcessPoolExecutor() as executor:
        worker_prime_list_in_list = list(executor.map(add_prime_num_to_queue, sub_start_end_list))
    flat_prime_list = [num for sublist in worker_prime_list_in_list for num in sublist]
    flat_prime_list.sort()
    print(f"There are total of {len(flat_prime_list)} prime numbers")
    print(f"First 10 prime numbers are: {flat_prime_list[:10]}")
    print(f"Last 10 prime numbers are: {flat_prime_list[-10:]}")

def add_prime_num_to_queue(start_end):
    process_list = []
    start, end = start_end
    for i in range(start,end+1):
        if is_prime(i):
            process_list.append(i)
    return process_list


if __name__ == "__main__":
    start = time.time()
    main(1,200)
    print(f"All took total of {time.time() - start:.2f} seconds")
