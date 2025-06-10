#Yeah I coded multiprocessing, the number increase at much higher rate than normal exponential since its multiplied the previous multiplied results
#Why this code must be run directly because when we initialize each process, its handled by OS and import the script again, doing this will prevent loop crash
from multiprocessing import Process
import time
def calculate_high_num(a):
    print(f"Calculating result of {a} to the very high num")
    for i in range(9):
        a *= a
    print(f"Result is {a}")

if __name__ == "__main__":
    start = time.time()
    p1 = Process(target=calculate_high_num, args=(2,))
    p2 = Process(target=calculate_high_num, args=(3,))
    p3 = Process(target=calculate_high_num, args=(4,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


    print(f"Total time took is {time.time() - start:.2f} seconds")