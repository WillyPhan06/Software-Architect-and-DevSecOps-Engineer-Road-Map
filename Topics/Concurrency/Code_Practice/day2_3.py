#Threads run within the code itself with shared memory
import threading
import time

counter = 0  # Shared variable

def increment():
    global counter
    for _ in range(5):
        temp = counter
        temp += 1
        time.sleep(0.1)  # Simulate some delay
        counter = temp
        print(f"Thread {threading.current_thread().name} incremented counter to {counter}")

if __name__ == "__main__":
    t1 = threading.Thread(target=increment, name="T1")
    t2 = threading.Thread(target=increment, name="T2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Final counter value: {counter}")
