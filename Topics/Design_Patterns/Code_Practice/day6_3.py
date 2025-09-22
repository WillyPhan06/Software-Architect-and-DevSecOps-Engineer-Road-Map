# Chaining decorators for example of authorization, validation, and timing. Now understood about the decorator factory, like when you do a decorator that passes a parameter, might as well still add a decorator then @wraps(func)
from functools import wraps
import time

def authorize(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user != role:
                raise PermissionError(f"{user} not allowed!")
            print("Authorized")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

def legalize(key):
    def decorator(func):
        @wraps(func)
        def wrapper(user, data,*args, **kwargs):
            if key != data.get("secret"):
                raise ValueError("Invalid key!")
            print("Data is legal")
            return func(user, data,*args, **kwargs)
        return wrapper
    return decorator

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed in {time.time() - start:.4f}s")
        return result
    return wrapper

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
@timing
@legalize(100)
@authorize("admin")
def sensitive_operation(user, data):
    print(f"Processing {data}...")


if __name__ == "__main__":
    sensitive_operation("admin", {"secret": 42})
    sensitive_operation("guest", {"secret": 50})  # This should raise a PermissionError
    sensitive_operation("admin", {"secret":99})  # This should raise a ValueError
    sensitive_operation("admin", {"secret": 100})  # This should work fine
