#Overriding copy and deepcopy methods in a dataclass

from dataclasses import dataclass, field
from copy import copy, deepcopy
from typing import List, Any

@dataclass
class Shape:
    name: str
    points : List[tuple] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def __copy__(self):
        cls = self.__class__
        new = cls.__new__(cls)
        new.name = self.name
        new.points = self.points
        new.metadata = self.metadata
        return new
    
    def __deepcopy__(self, memo: dict):
        cls = self.__class__
        new = cls.__new__(cls)
        memo[id(self)] = new
        new.name = deepcopy(self.name, memo)
        new.points = deepcopy(self.points, memo)
        new.metadata = deepcopy(self.metadata, memo)
        return new
    
if __name__ == "__main__":
    org_shape = Shape(
        name="Triangle",
        points=[(0, 0), (1, 0), (0, 1)],
        metadata={"color": "red"}
    )

    shallow_copied_shape = copy(org_shape)
    deep_copied_shape = deepcopy(org_shape)

    org_shape.points.append((1, 1))
    org_shape.name = "Modified Triangle"
    
    print("Original Shape Points:", org_shape.points)
    print("Shallow Copied Shape Points:", shallow_copied_shape.points)
    print("Deep Copied Shape Points:", deep_copied_shape.points)
    print("Original Shape Name:", org_shape.name)
    print("Shallow Copied Shape Name:", shallow_copied_shape.name)
    print("Deep Copied Shape Name:", deep_copied_shape.name)