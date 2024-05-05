from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def set_next_handler(self, next_handler):
        pass

    @abstractmethod
    def handle(self, score):
        pass


class HandlerManage(AbstractHandler):
    _next_handler = None

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler
        return next_handler

    @abstractmethod
    def handle(self, score):
        if self._next_handler:
            return self._next_handler.handle(score)
        return None


class HandleOne(HandlerManage):
    def handle(self, score):
        if 1 <= score < 10:
            return f'{self.__class__.__name__} handled this requests -> {score}'
        else:
            return super().handle(score)


class HandleTwo(HandlerManage):
    def handle(self, score):
        if 10 <= score < 20:
            return f'{self.__class__.__name__} handled this requests -> {score}'
        else:
            return super().handle(score)


class DefualtHandle(HandlerManage):
    def handle(self, score):
        return f'{self.__class__.__name__} handled this requests -> {score}'


def clinet(handler, scores: list):
    for score in scores:
        print(handler.handle(score))


score_list = [5, 1, 10, 2, 3, 50]
h1 = HandleOne()
h2 = HandleTwo()
defualt_handler = DefualtHandle()
h1.set_next_handler(h2).set_next_handler(defualt_handler)
clinet(h1, score_list)