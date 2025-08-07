#Create 2 functions of writing and reading to count word count for each file then benchmark time of each small functions and total time to ran all
#Total time was 0.01s while sum time of all functions is 0.03s, which showcase x3 speed in concurrency using thread to play around with writing and reading files
from concurrent.futures import ThreadPoolExecutor
import os
import threading
import time

lock = threading.Lock()

file_place = r"C:\Users\Someone\Downloads"
files = ["cat.txt","dog.txt","human.txt","baba.txt","mama.txt"]
word_count_dic = {}
task_caw_time_dic = {}
task_rac_time_dic = {}

def create_and_write_file(file_name):
    global task_caw_time_dic
    start = time.time()
    real_path = os.path.join(file_place,file_name)
    print(f"CAW opening path: {real_path}")
    with open(real_path,"w",encoding="utf-8") as file:
        file.write(f"There is once a little {file_name[:-4]} climbing on the tree")
    print(f"CAW done writing: {real_path}")
    task_caw_time_dic[file_name] = time.time() - start

def read_and_count_word(file_name):
    global word_count_dic, task_rac_time_dic
    start = time.time()
    real_path = os.path.join(file_place, file_name)
    print(f"RAC opening path: {real_path}")
    with open(real_path, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.strip().split():
                with lock:
                    if word.lower() in word_count_dic:
                        word_count_dic[word.lower()] += 1
                        print(f"RAC added count for: {word.lower()}. Current count: {word_count_dic[word.lower()]}")
                    else:
                        word_count_dic[word.lower()] = 1
                        print(f"RAC added word: {word.lower()}")
    task_rac_time_dic[file_name] = time.time() - start


start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(create_and_write_file, files)
    executor.map(read_and_count_word, files)
end = time.time() - start
for word, count in sorted(word_count_dic.items(), key=lambda x: x[1], reverse=True):
    print(f"Word: {word}. Count: {count}")

for file, time in task_caw_time_dic.items():
    print(f"CAW task: {file} took {time} seconds.")
for file2, time2 in task_rac_time_dic.items():
    print(f"RAC task {file2} took {time2} seconds.")
print(f"All took total of {end} seconds")
