from dataclasses import dataclass

quantity = 100

@dataclass
class Laptop:
    brand: str
    price: int


# Naive creation
laptops = [Laptop("MSi", 1000) for i in range(quantity)]

# Flyweight approach

class LaptopFactory:
    intrinsic = {}

    @classmethod
    def get_intrinsic(cls, *args):
        key = tuple(args)
        inst = cls.intrinsic.get(key)
        if inst is None:
            inst = Laptop(*args)
            cls.intrinsic[key] = inst
        return inst
    
laptops_2 = []

for i in range(quantity):
    laptop = LaptopFactory.get_intrinsic("MSi", 1000)
    laptops_2.append(laptop)

print(len(laptops))
print(len(laptops_2))
