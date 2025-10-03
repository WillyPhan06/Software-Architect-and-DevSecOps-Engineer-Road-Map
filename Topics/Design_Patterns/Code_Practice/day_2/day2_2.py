# Make the Singleton Pattern thread-safe
import threading

class SingletonObject:
    _instance = None
    _thread_lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._thread_lock:
                cls._instance = super(SingletonObject, cls).__new__(cls)
        return cls._instance
