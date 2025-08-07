#Simulating running thread in parallel then catch signal and report back the latest undone task gracefully
from concurrent.futures import ThreadPoolExecutor
import signal
import time
import sys

terminate = False
latest_i = -1
def save_latest_task_order(i):
    print(f"Saved latest undone task order {i}")


def do_delay_stuff(i):
    global latest_i
    print(f"Task {i} start doing delay stuff")
    time.sleep(1 + 0.5*i)
    if not terminate:
        print(f"Task {i} done doing delay stuff")
        latest_i = i + 1


def handle_exit(signum, frame):
    global terminate, latest_i
    signal_dic = {signal.SIGINT: "Received user stop signal", signal.SIGTERM: "Received program termination"}
    print(f"{signal_dic.get(signum,'Unknown stop signal')}")
    print("Saving now")
    save_latest_task_order(latest_i)
    print("Closing now")
    terminate = True
    sys.exit()


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)


tasks = [i for i in range(1,11)]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(do_delay_stuff,tasks)