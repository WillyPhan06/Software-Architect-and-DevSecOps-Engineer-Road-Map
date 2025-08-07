#Process doesn't share memory, it just take a copy of the script via importing
from multiprocessing import Process
import time
from multiprocessing import current_process

counter = 0  # This variable is NOT shared across processes

def increment():
    global counter
    for _ in range(5):
        temp = counter
        temp += 1
        time.sleep(0.1)
        counter = temp
        print(f"Process {current_process().name} incremented counter to {counter}")

if __name__ == "__main__":
    from multiprocessing import current_process

    p1 = Process(target=increment, name="P1")
    p2 = Process(target=increment, name="P2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Final counter value: {counter}")  # Still 0 here, processes do not share memory
