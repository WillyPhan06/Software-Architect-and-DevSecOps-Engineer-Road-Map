# Goal: Make this become Singleton

# class Logger:
#     def __init__(self):
#         print("Logger created")

#     def log(self, message):
#         print(f"[LOG]: {message}")

class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def log(self, message):
        print(f"[LOG]: {message}")




