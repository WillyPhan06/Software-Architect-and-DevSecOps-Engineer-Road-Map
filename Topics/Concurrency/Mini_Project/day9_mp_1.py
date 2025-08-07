#This is the sequential approach to calculating prime number count from 1 to 10M
#Result is accurate prime number count of 664579 but took up to 225.02 seconds, about 3 time slower than multiprocessing method
from .day9_mp import count_prime_num
import time

the_range = (1,10000001)
start = time.time()
total_count = count_prime_num(the_range)
print(f"All took total of {time.time() - start:.2f} seconds")
print(f"Total count is {total_count}")