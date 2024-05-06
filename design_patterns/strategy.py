from abc import ABC, abstractmethod


class Strategy:
    def __init__(self, setntence):
        self._sentence = setntence
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def run(self):
        return self._strategy.direct(self._sentence)


class AbstractDirection(ABC):
    @abstractmethod
    def direct(self, sentence):
        pass


class Right(AbstractDirection):
    def direct(self, sentence):
        return sentence[::-1]

class Left(AbstractDirection):
    def direct(self, sentence):
        return sentence[::1]


a = Strategy('hello')
a.set_strategy(Left())
print(a.run())