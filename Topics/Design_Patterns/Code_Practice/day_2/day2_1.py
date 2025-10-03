#Basic Singleton Pattern Implementation, but not the pythonic approach, or at least not for beginners

class SingletonObject:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonObject,cls).__new__(cls)
        return cls._instance
    
