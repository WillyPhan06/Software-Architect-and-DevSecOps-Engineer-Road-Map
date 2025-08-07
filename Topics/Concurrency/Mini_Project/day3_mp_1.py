#Applied threading and Rlock, since it's a for very niche design, not so efficient, same execution time
import threading
import time

process_lock = threading.RLock()

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        with process_lock:
            self.balance += amount
        time.sleep(0.1)
        with process_lock:
            print(f"Success deposit for {self.name}. Old balance: {self.balance - amount}. New balance: {self.balance}. Deposit amount: {amount}")
    def withdraw(self, amount):
        if self.balance >= amount:
            with process_lock:
                self.balance -= amount
            time.sleep(0.1)
            print(f"Success withdraw for {self.name}. Old balance: {self.balance + amount}. New balance: {self.balance}. Withdraw amount: {amount}")
        else:
            time.sleep(0.1)
            print("Balance not sufficient to withdraw")
    def show_balance(self):
        print(f"Current balance of {self.name} is {self.balance}")

def outside_deposit(account):
    with process_lock:
        for i in range(10):
            account.deposit(100)

name_list = ["Bill", "Willy", "Ben", "Baba", "Bubu", "Hehe", "Haha", "Mama", "Dada", "Sir"]
account_list = []
threads = []

start = time.time()
for name in name_list:
    account = BankAccount(name)
    account_list.append(account)

for account in account_list:
    t = threading.Thread(target=outside_deposit, args=(account,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

for account in account_list:
    account.show_balance()


print(f"Total time took: {time.time() - start:.2f} seconds")