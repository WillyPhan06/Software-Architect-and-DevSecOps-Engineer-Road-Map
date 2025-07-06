#This is set trace to know the event, function, and place what's going on for debug
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def tracing(frame,event,args):
    print(f"Event: {event}. Function: {frame.f_code.co_name}. Place: {frame.f_globals.get("__name__")}")
    return tracing

def main(i):
    print(f"Task {i} starting to do")
    time.sleep(0.5)
    print(f"Task {i} done")

threading.settrace(tracing)
tasks = [i for i in range(1,3)]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(main,tasks)



