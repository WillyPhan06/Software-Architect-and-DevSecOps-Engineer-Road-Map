#Basically the code above with added with the singal.signal(signal.SIGTERM, handle_terminate)
import signal
import sys
import time

def save_progress(current_count):
    print(f"Saved progress of current count: {current_count}")


def handle_exit(signum, frame):
    print("Saving progress...")
    save_progress(count)
    print("Closing now...")
    sys.exit()

def handle_terminate(signum, frame):
    print("Program has been terminated! Saving now...")
    save_progress(count)
    print("Closing now...")
    sys.exit()

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_terminate)

count = 0
while True:
    count+=1
    print(f"Grinded up to {count}")
    print("Upgrading...")
    time.sleep(0.5)
    print("Done upgrade!")