#Optimized using just 1 lock per function to reduce overhead
import threading
import time
from concurrent.futures import ThreadPoolExecutor
lock = threading.Lock()

div2 = 0
div3 = 0
div5 = 0

def check_div(n):
    global div2, div3, div5
    time.sleep(0.1)
    is_div_2 = n % 2 == 0
    time.sleep(0.1)
    is_div_3 = n % 3 == 0
    time.sleep(0.1)
    is_div_5 = n % 5 == 0
    with lock:
        if is_div_2:
            div2 += 1
        if is_div_3:
            div3 += 1
        if is_div_5:
            div5 += 1

start = time.time()
tasks = [i for i in range(1,101)]
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(check_div, tasks)

print(f"Div 2: {div2}")
print(f"Div 3: {div3}")
print(f"Div 5: {div5}")
print(f"All took total of {time.time() - start:.2f} seconds")