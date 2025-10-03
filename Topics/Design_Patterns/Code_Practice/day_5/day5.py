#Coded again Prototype Design Pattern from understanding again, basically there are 2 types of copy, one is shallow copy which for fields like list or dict it still shares while deep copy creates a new instance of those fields as is.

from dataclasses import dataclass, field
from copy import copy, deepcopy
from typing import List


@dataclass
class Shape:
    name: str
    points: List[tuple] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def shallow_copy(self):
        return copy(self)
    
    def deep_copy(self):
        return deepcopy(self)
    
if __name__ == "__main__":
    org_shape = Shape(
        name="Triangle",
        points=[(0, 0), (1, 0), (0, 1)],
        metadata={"color": "red"}
    )

    shallow_copied_shape = org_shape.shallow_copy()
    deep_copied_shape = org_shape.deep_copy()

    org_shape.points.append((1, 1))
    org_shape.name = "Modified Triangle"
    
    print("Original Shape Points:", org_shape.points)
    print("Shallow Copied Shape Points:", shallow_copied_shape.points)
    print("Deep Copied Shape Points:", deep_copied_shape.points)
    print("Original Shape Name:", org_shape.name)
    print("Shallow Copied Shape Name:", shallow_copied_shape.name)
    print("Deep Copied Shape Name:", deep_copied_shape.name)