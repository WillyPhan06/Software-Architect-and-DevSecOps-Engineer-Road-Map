# Goal: Apply DRY (Don't Repeat Yourself)
# def calculate_area_rectangle(length, width):
#     return length * width

# def calculate_area_square(side):
#     return side * side

# def print_rectangle_area(length, width):
#     area = length * width
#     print(f"Rectangle area is: {area}")

# def print_square_area(side):
#     area = side * side
#     print(f"Square area is: {area}")

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_square(side):
    return side ** 2

def print_area(shape, area):
    print(f"{shape} area is: {area}")

