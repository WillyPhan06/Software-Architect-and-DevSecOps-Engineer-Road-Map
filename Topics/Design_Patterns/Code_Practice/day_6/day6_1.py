# Added the decorator to another function as well as understanding why @wraps is used for the metadata preservation
# py_decorator.py
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    add(3, 4)
    multiply(5, 6)
