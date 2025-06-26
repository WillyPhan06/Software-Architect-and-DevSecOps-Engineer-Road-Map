#Benchmark CPU task for multiprocessing for 10k tasks of calculating fibonacci of the number of the nth position in the fibonacci
#Took 8 - 9 seconds, super fast since all calculation are started in new processes in independent CPU cores, the print inside the function is quite expensive so by making the print inside the main function, successfully decreased from 10 - 12 to only 8 - 9 seconds
import time
from concurrent.futures import ProcessPoolExecutor

def fibonacci(n):
    if n <= 2:
        return 1
    first = 1
    second = 1
    for i in range(2,n):
        third = first + second
        first = second
        second = third
    return third

if __name__ == "__main__":
    start = time.time()
    tasks = [i for i in range(1,10001)]
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(fibonacci,tasks))
    for result in results:
        print(result)
    print(f"All took total of {time.time() - start:.2f} seconds")