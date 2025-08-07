#Benchmark CPU task for threading for 10k tasks of calculating fibonacci of the number of the nth position increasing from 1 to 10k
#Took 13.8 - 14 seconds
import time
from concurrent.futures import ThreadPoolExecutor

def fibonacci(n):
    if n <= 2:
        print(1)
        return
    first = 1
    second = 1
    for i in range(2,n):
        third = first + second
        first = second
        second = third
    print(third)

start = time.time()
tasks = [i for i in range(1,10001)]
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(fibonacci,tasks)
print(f"All took total of {time.time() - start:.2f} seconds")
