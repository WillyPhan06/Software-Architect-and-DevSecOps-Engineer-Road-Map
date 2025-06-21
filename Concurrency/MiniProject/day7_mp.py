#So this is my mini project using threading and queue to download images via random image link then save to a folder via producer threads then the consumer threads will take those images and thumbnail them then save to a new folder, in here i initialized 10 producer threads with 1 consumer thread doing total work of 1.2 seconds in average.
import threading
import os
import time
from PIL import Image
from io import BytesIO
import random
import requests
import queue

url_list = [f"https://picsum.photos/200/300?random={random.randint(1,100)}" for i in range(10)]
buffer = queue.Queue(maxsize=100)
lock = threading.Lock()
buffer_put_count = 0


producer_output_file = r"YourPath\random_web_pics"
consumer_output_file = r"YourPath\random_web_pics_thumbnail"

os.makedirs(r"YourPath\random_web_pics", exist_ok=True)
os.makedirs(r"YourPath\random_web_pics_thumbnail", exist_ok=True)

def producer_task(i, url):
    global buffer_put_count
    print(f"Started producer task {i}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_path = os.path.join(producer_output_file,f"image_{i}.jpg")
        print(f"Created new image path for task {i}: {image_path}")
        with Image.open(BytesIO(response.content)) as img:
            img.save(image_path)
        print(f"Task {i} successfully saved image to: {image_path}")
        buffer.put(image_path)
        with lock:
            buffer_put_count += 1
            print(f"Increased buffer put count to {buffer_put_count}")
        print(f"Task {i} put image_{i}.jpg to the buffer")
        if buffer_put_count == len(url_list):

            print("INITIALIZED STOP SIGNAL")
            buffer.put("STOP_NOW_CONSUMER_FUNCTION_!")


    except Exception as e:
        print(f"Failed in producer task {i}: {e}")

def consumer_task():

    while True:

        try:
            item = buffer.get(timeout=10)
            if item == "STOP_NOW_CONSUMER_FUNCTION_!":
                print("Received Stop Signal! Stopping now!")
                buffer.task_done()
                break

        except queue.Empty:
            print(f"Consumer task stopped via timeout")
            break

        try:
            with Image.open(item) as img:
                img.thumbnail((100,100))
                thumbnail_image_path = os.path.join(consumer_output_file, item[len(producer_output_file)+1:])
                print(f"Consumer task created thumbnail image path: {thumbnail_image_path}")
                img.save(thumbnail_image_path)
                print(f"Consumer task saved: {thumbnail_image_path}")
        except Exception as e:
            print(f"Failed in consumer task: {e}")
        finally:
            buffer.task_done()

producer_thread_list = []


start = time.time()
consumer_thread = threading.Thread(target=consumer_task)
consumer_thread.start()
for i, url in enumerate(url_list,1):
    producer_thread = threading.Thread(target=producer_task, args=(i,url))

    producer_thread_list.append(producer_thread)

    producer_thread.start()


for thread in producer_thread_list:
    thread.join()

print("Done Producer Wait")

buffer.join()

print("Done Buffer Wait")

print(f"Successfully resize images in total of {time.time() - start:.2f} seconds")