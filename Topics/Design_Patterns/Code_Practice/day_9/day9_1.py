# Not only it works with classes but also with functions as well

# observer/pythonic_observer.py

class Event:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)

    def unsubscribe(self, fn):
        self._subscribers.remove(fn)

    def notify(self, *args, **kwargs):
        for fn in self._subscribers:
            fn(*args, **kwargs)

# Usage
def email_handler(msg):
    print(f"Email: {msg}")

def sms_handler(msg):
    print(f"SMS: {msg}")


if __name__ == "__main__":
    event = Event()
    event.subscribe(email_handler)
    event.subscribe(sms_handler)
    event.notify("Python Observer Pattern!")
    event.unsubscribe(email_handler)
    event.notify("Screw you email")
