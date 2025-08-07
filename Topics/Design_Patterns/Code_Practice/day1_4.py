# Goal: Apply Liskov Substitution Principle (LSP) in SOLID
# ❌ LSP Violation
# class Bird:
#     def fly(self):
#         print("Bird is flying")

# class Ostrich(Bird):
#     def fly(self):
#         raise Exception("Ostriches can't fly!")

from abc import ABC, abstractmethod

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass
class Runner(ABC):
    @abstractmethod
    def run(self):
        pass

class Ostrich(Runner):
    def run(self):
        print("Ostrich is running")

