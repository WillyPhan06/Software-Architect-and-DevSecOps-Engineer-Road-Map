#Recreating Abstract Factory Pattern with Shapes and Drawing Tools

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

@dataclass
class Circle(Shape):
    radius: float

    def draw(self) -> str:
        return f"Drawing a circle with radius {self.radius}"
    
@dataclass
class Square(Shape):
    side: float

    def draw(self) -> str:
        return f"Drawing a square with side {self.side}"
    
class DrawingToolFactory(ABC):
    @abstractmethod
    def create_blueprint(self, shape: Shape) -> str:
        pass

class PenToolFactory(DrawingToolFactory):
    def create_blueprint(self, shape: Shape) -> str:
        return f"Pen tool: {shape.draw()}"
    
class BrushToolFactory(DrawingToolFactory):
    def create_blueprint(self, shape: Shape) -> str:
        return f"Brush tool: {shape.draw()}"
    
def client_run_code(factory: DrawingToolFactory, shape: Shape) -> None:
    blueprint = factory.create_blueprint(shape)
    print(blueprint)

client_run_code(PenToolFactory(), Circle(radius=5))
client_run_code(BrushToolFactory(), Square(side=10))



