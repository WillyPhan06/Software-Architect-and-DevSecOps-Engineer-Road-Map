# Implementing a decorator for Adapter pattern and run client code

# Suppose new API changed method name from `fetch()` -> `get()`
from functools import wraps

# A decorator function for telling it's calling from Adapter
def adapter_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling via Adapter for {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def old_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling from legacy code {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class OldApiClient:
    @old_call
    def fetch(self, key: str) -> str:
        return f"old:{key}"

class NewApiWrapper:
    def __init__(self, old_client: OldApiClient):
        self._old = old_client
    @adapter_call
    def get(self, key: str) -> str:
        return self._old.fetch(key)
    
if __name__ == "__main__":
    old_api_client = OldApiClient()
    new_api_wrapper = NewApiWrapper(old_api_client)
    print(new_api_wrapper.get("my_key"))
    

