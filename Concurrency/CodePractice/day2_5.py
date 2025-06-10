#Subclass Thread
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, task_id):
        super().__init__()  # call the base class constructor
        self.task_id = task_id

    def run(self):
        print(f"Task {self.task_id} is starting...")
        time.sleep(2)
        print(f"Task {self.task_id} is done!")

# Create and start threads
threads = []
for i in range(5):
    t = MyThread(i)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All threads are finished.")
