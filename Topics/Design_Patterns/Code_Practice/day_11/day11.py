# Instantiating and execute command as well as undo it, as well as understanding the Command Pattern helps with decoupling the code

from abc import ABC, abstractmethod

# Receiver
class Light:
    def on(self):
        print("Light is ON")
    def off(self):
        print("Light is OFF")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    def undo(self):
        pass  # optional

# Concrete commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.history = []

    def press(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
        else:
            print("Can't undo because no previous action")

if __name__ == "__main__":
    light = Light()
    remote_control = RemoteControl()
    light_on_command = LightOnCommand(light)
    remote_control.press(light_on_command)
    for i in range(3):
        remote_control.undo()