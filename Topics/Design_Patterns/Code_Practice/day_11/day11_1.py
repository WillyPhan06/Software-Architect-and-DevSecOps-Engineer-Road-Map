# Pythonic approach passing callable of Command Pattern
# command/pythonic_command.py
from typing import Callable, List

class Invoker:
    def __init__(self):
        self.history: List[Callable[[], None]] = []

    def execute(self, command: Callable[[], None], undo: Callable[[], None] = None):
        command()
        if undo:
            self.history.append(undo)

    def undo(self):
        if self.history:
            undo_fn = self.history.pop()
            undo_fn()

# Usage
light_state = {"on": False}
def light_on():
    light_state["on"] = True
    print("Light ON")
def light_off():
    light_state["on"] = False
    print("Light OFF")


if __name__ == "__main__":
    invoker = Invoker()
    invoker.execute(light_on, light_off)
    invoker.undo()
    invoker_2 = Invoker()
    invoker.execute(light_on)
    invoker.undo()
