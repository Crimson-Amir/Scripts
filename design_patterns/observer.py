from abc import ABC, abstractmethod
from random import randrange

class AbstractPublisher(ABC):

    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass


    @abstractmethod
    def notif_observers(self):
        pass


class Publisher(AbstractPublisher):
    _observers = []
    event_number = None


    def subscribe(self, *observers):
        for observer in observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notif_observers(self):
        for observer in self._observers:
            observer.update(self)

    def events(self):
        random_num = randrange(1, 10)
        self.event_number = random_num
        self.notif_observers()


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, object_):
        pass


class ObserverOne(AbstractObserver):
    def update(self, object_):
        if object_.event_number > 5:
            print(f'{self.__class__.__name__} handled number')


class ObserverTwo(AbstractObserver):
    def update(self, object_):
        if object_.event_number <= 5:
            print(f'{self.__class__.__name__} handled number')


event_1 = ObserverOne()
event_2 = ObserverTwo()

publisher = Publisher()
publisher.subscribe(event_1, event_2)

publisher.events()