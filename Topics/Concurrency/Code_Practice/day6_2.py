#Example of applying ProcessPoolExecutor in a demo heavy computing task using map and random int
from concurrent.futures import ProcessPoolExecutor
import time
import random

def calculate_super_large(num):
    org_num = num
    print(f"Start calculating number: {num}")
    task_start = time.time()
    for i in range(9):
        num *= num
    print(f"Task done calculating number: {org_num} in {time.time() - task_start:.2f} seconds, which has result: {num}")

if __name__ == "__main__":
    random_num_list = [random.randint(1,5) for i in range(10)]
    start = time.time()
    with ProcessPoolExecutor(max_workers=len(random_num_list)) as executor:
        executor.map(calculate_super_large, random_num_list)
    print(f"All took total of {time.time() - start:.2f} seconds")