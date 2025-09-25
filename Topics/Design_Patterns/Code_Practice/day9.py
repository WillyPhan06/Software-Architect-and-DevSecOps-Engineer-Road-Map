#Instantiating a subject then attach observers in and when the subject notifies something, all the observers in the list of observers of the subject get notified

from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete observers
class EmailObserver(Observer):
    def update(self, message: str):
        print(f"Email received: {message}")

class SMSObserver(Observer):
    def update(self, message: str):
        print(f"SMS received: {message}")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    @abstractmethod
    def detach(self, observer: Observer):
        pass
    @abstractmethod
    def notify(self, message: str):
        pass

# Concrete Subject
class NewsPublisher(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for obs in self._observers:
            obs.update(message)

# Client Code
if __name__ == "__main__":
    news_publisher = NewsPublisher()
    email_observer = EmailObserver()
    sms_observer = SMSObserver()

    news_publisher.attach(email_observer)
    news_publisher.attach(sms_observer)

    news_publisher.notify("Hehe bois")

    news_publisher.detach(email_observer)

    news_publisher.notify("Screw you email")



