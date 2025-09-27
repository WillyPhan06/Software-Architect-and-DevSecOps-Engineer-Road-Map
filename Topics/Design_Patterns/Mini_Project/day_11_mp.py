# Applied command pattern into a maze going program with help of Prototype Pattern to deepcopy previous maze display
from dataclasses import dataclass, field
from typing import List
from abc import ABC, abstractmethod
import copy


# ------------------------------
# Maze (game state)
# ------------------------------
@dataclass
class Maze:
    rows: int = 7
    cols: int = 7
    char_shape: str = "@"
    char_pos: List[int] = field(default_factory=lambda: [1, 1])
    maze: List[List[str]] = field(init=False)
    ogma: List[List[str]] = field(init=False)

    def __post_init__(self):
        # build outer wall
        self.ogma = [
            ["*" if r in (0, self.rows - 1) or c in (0, self.cols - 1) else " "
             for c in range(self.cols)]
            for r in range(self.rows)
        ]
        self.maze = copy.deepcopy(self.ogma)

    def reset(self):
        self.maze = copy.deepcopy(self.ogma)

    def plug_char_pos(self) -> bool:
        """Place character in maze; return False if out of bounds."""
        self.reset()
        r, c = self.char_pos
        if 0 < r < self.rows - 1 and 0 < c < self.cols - 1:
            self.maze[r][c] = self.char_shape
            return True
        return False


# ------------------------------
# Maze Display (output)
# ------------------------------
@dataclass
class MazeDisplay:
    maze: Maze

    def render(self):
        for line in self.maze.maze:
            print(" ".join(line))
        print()  # blank line for readability


# ------------------------------
# Command Pattern
# ------------------------------
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


@dataclass
class MoveCommand(Command):
    move_key: str
    maze: Maze

    def execute(self):
        if self.move_key == "w":
            self.maze.char_pos[0] -= 1
        elif self.move_key == "a":
            self.maze.char_pos[1] -= 1
        elif self.move_key == "s":
            self.maze.char_pos[0] += 1
        elif self.move_key == "d":
            self.maze.char_pos[1] += 1
        else:
            print("INVALID KEY")

    def undo(self):
        # inverse of execute
        if self.move_key == "w":
            self.maze.char_pos[0] += 1
        elif self.move_key == "a":
            self.maze.char_pos[1] += 1
        elif self.move_key == "s":
            self.maze.char_pos[0] -= 1
        elif self.move_key == "d":
            self.maze.char_pos[1] -= 1


# ------------------------------
# Invoker (handles history)
# ------------------------------
@dataclass
class Invoker:
    history: List[Command] = field(default_factory=list)

    def execute(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()


# ------------------------------
# Main Game
# ------------------------------
class Main:
    def start(self):
        char_shape = input("Please enter your char shape: ")
        maze = Maze(char_shape=char_shape)
        display = MazeDisplay(maze)
        invoker = Invoker()

        maze.plug_char_pos()
        display.render()

        while True:
            choice = input("Enter move (w/a/s/d), undo (u), or quit (q): ").lower()
            if choice in ["w", "a", "s", "d"]:
                cmd = MoveCommand(choice, maze)
                invoker.execute(cmd)
            elif choice == "u":
                invoker.undo()
            elif choice == "q":
                print("Bye!")
                break
            else:
                print("INVALID KEY")
                continue

            if not maze.plug_char_pos():
                print("YOU WENT OUT OF BORDER. YOU LOST!")
                break

            display.render()


# ------------------------------
# Run
# ------------------------------
if __name__ == "__main__":
    main = Main()
    main.start()
