# Goal: Apply Dependency Inversion Principle (DIP) in SOLID
# # ❌ DIP Violation
# class MySQLDatabase:
#     def connect(self):
#         print("Connected to MySQL")

# class App:
#     def __init__(self):
#         self.db = MySQLDatabase()

#     def start(self):
#         self.db.connect()

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class App:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()