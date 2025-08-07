#This is the multiprocessing method using ProcessPoolExecutor to calculate prime number count from 1 to 10M
#Result is accurate prime number count of 664579 and took only 71.72 seconds, about 3 time faster than the sequential approach
#Ideal speed should be faster than 4 times since its 4x more CPU cores, but since such overhead, x3 speed is practical and expected in real life scenarios
from .day9_mp import count_prime_num
from concurrent.futures import ProcessPoolExecutor
import time

if __name__ == "__main__":
    ranges = [(1, 2500001), (2500001, 5000001), (5000001, 7500001), (7500001, 10000001)]
    start = time.time()
    with ProcessPoolExecutor() as executor:
        result_list = executor.map(count_prime_num,ranges)

    total_count = sum(result_list)
    print(f"All took total of {time.time() - start:.2f} seconds")
    print(f"Total prime number count is {total_count}")