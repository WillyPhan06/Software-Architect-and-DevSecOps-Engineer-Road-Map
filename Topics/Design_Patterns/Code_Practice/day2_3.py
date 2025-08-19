# Make Singleton using decorator approach

def singleton(cls):
    instances = {}

    def get_instances(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instances

@singleton
class Logger:
    pass