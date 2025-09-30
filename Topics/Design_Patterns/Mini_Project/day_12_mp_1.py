from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class S(Enum):
    STATIONARY = auto()
    IN_MOTION = auto()

BEHAVIOR_DICT = {
    (S.STATIONARY, "accelerating") : (S.IN_MOTION, lambda: print("Bro standing now starting to making it real by accelerating")),
    (S.STATIONARY, "breaking") : (S.STATIONARY, lambda: print("What bro tryna do? Stop while stopping?")),
    (S.IN_MOTION, "accelerating") : (S.IN_MOTION, lambda: print("GAS GAS GAS I'M GONNA STEP ON THE GAS TONIGHT WE WILL RIDE FOREVER")),
    (S.IN_MOTION, "breaking") : (S.STATIONARY, lambda: print("Oh why bro slowing down now? We ain't ballin no more?"))
}

@dataclass
class Car:
    state: Any

    def trigger(self, event, *args):
        key = (self.state, event)
        if key not in BEHAVIOR_DICT:
            print("NOPE!")
            return

        state, action = BEHAVIOR_DICT[key]
        if action:
            action()
        self.state = state

if __name__ == "__main__":
    my_car = Car(state=S.STATIONARY)
    my_car.trigger("accelerating")
    my_car.trigger("accelerating")
    my_car.trigger("breaking")
    my_car.trigger("breaking")
    my_car.trigger("accelerating")
    my_car.trigger("breaking")
    
        

