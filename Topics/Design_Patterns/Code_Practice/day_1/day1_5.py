# Goal: Apply Interface Segregation Principle (ISP) in SOLID
# ❌ ISP Violation
# class Worker:
#     def work(self):
#         pass

#     def eat(self):
#         pass

# class Robot(Worker):
#     def work(self):
#         print("Robot working")

#     def eat(self):
#         # Robots don't eat
#         pass

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class RobotWorker(Worker):
    def work(self):
        print("Robot working")

class HumanWorker(Worker, Eater):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")