from abc import ABC, abstractmethod
from dataclasses import dataclass

class State(ABC):
    @abstractmethod
    def accelerating(self, car):
        pass

    @abstractmethod
    def breaking(self, car):
        pass

class Stationary(State):
    def accelerating(self, car):
        print("Car stating to accelerate")
        car.state = InMotion()

    def breaking(self, car):
        print("Car already not moving, what is bro tryna do")

class InMotion(State):
    def accelerating(self, car):
        print("Car already in motion now moving even faster")

    def breaking(self, car):
        print("Car slowing down now due to break")
        car.state = Stationary()

@dataclass
class Car:
    state : State

    def accelerating(self):
        self.state.accelerating(self)

    def breaking(self):
        self.state.breaking(self)


if __name__ == "__main__":
    ini_state = Stationary()
    car = Car(ini_state)
    car.accelerating()
    car.accelerating()
    car.breaking()
    car.breaking()
    car.accelerating()
    car.breaking()



        