#Code From Scratch Threading Without Look.
import threading
import time

print_lock = threading.Lock()

def calculate_multiply(a,b):
    with print_lock:
        print(f"Calculating result of {a} and {b} multiplication")
    time.sleep(5)
    with print_lock:
        print(f"Result is {a*b}")

start = time.time()
t1 = threading.Thread(target=calculate_multiply, args=(4,5))
t2 = threading.Thread(target=calculate_multiply, args=(5,6))
t3 = threading.Thread(target=calculate_multiply, args=(6,7))
t4 = threading.Thread(target=calculate_multiply, args=(7,8))
t5 = threading.Thread(target=calculate_multiply, args=(8,9))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(f"Total time took is {time.time() - start:.2f} seconds")