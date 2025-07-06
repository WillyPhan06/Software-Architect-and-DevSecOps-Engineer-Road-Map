#Simulating showing logging for debug for simple downloading web showcasing btyes downloaded, time took for each task and total time took
import logging
import time
from concurrent.futures import ThreadPoolExecutor
import requests
task_time_dic = {}
logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s] (%(threadName)s/%(name)s): %(message)s", datefmt="%H:%M:%S")

def do_task(i):
    global task_time_dic
    do_task_start = time.time()
    logging.debug(f"Doing task {i} downloading content from web")
    response = requests.get("https://example.com/")
    logging.debug(f"Done task {i} got {len(response.content)} bytes from the web")
    task_time_dic[i] = time.time() - do_task_start


start = time.time()
tasks = [i for i in range(1,11)]
with ThreadPoolExecutor(max_workers=10, thread_name_prefix="Worker") as executor:
    executor.map(do_task, tasks)
end = time.time() - start
for task, time in task_time_dic.items():
    logging.debug(f"Task: {task}. Time: {time}")
logging.debug(f"Total time: {end}")