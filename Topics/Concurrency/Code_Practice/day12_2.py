#Applied the try except into the code and actually stop the "Done upgrade" when user signal stop
import signal
import time


terminate = False

def save_progress(count):
    print(f"Saved current progress: {count}")

def handle_exit(signum, frame):
    global terminate
    signals = {signal.SIGINT: "Received user stop signal", signal.SIGTERM: "Received program stop signal"}
    print(f"{signals.get(signum, "Unknown signal happened")}")
    print("Saving current progress")
    save_progress(count)
    print("Closing program")
    terminate = True


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

count = 0
try:
    while not terminate:
        count += 1
        print(f"Grinded up to {count}")
        print("Upgrading...")
        for i in range(5):
            if terminate:
                break
            time.sleep(0.1)
        if not terminate:
            print("Upgraded!")

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("Finally")