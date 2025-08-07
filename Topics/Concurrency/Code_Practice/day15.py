#Practice with logging debug using ThreadPoolExecutor and name it using thread_name_prefix
import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s = %(message)s")

def main(i):
    logging.debug(f"Working on task {i}")
    time.sleep(0.5)
    logging.debug(f"Done working on task {i}")

tasks = [i for i in range(1,11)]
with ThreadPoolExecutor(max_workers=10, thread_name_prefix="Worker") as executor:
    executor.map(main,tasks)