from abc import ABC, abstractmethod

class AbstractMediator(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class MediatorOne(AbstractMediator):
    def __init__(self, sender, reciver):
        self.sender = sender
        self.sender.set_mediator(self)
        self.reciver = reciver
        self.reciver.set_mediator(self)

    def notify(self, message):
        self.reciver.recive(self.sender.__class__.__name__, message)


class AbstractComponent(ABC):
    def __init__(self, mediator = None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def recive(self, reciver, message):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class ComponentOne(AbstractComponent):
    def recive(self, reciver, message):
        print(f'recive {message} from {reciver}')

    def notify(self, message):
        self._mediator.notify(f'Hey Cuty')

    def do_job_one(self):
        print('i did job one')
        self.notify('ONE')


class ComponentTwo(AbstractComponent):
    def recive(self, reciver, message):
        print(f'recive {message} from {reciver}')

    def notify(self, message):
        self._mediator.notify(f'Hey Babe')

    def do_job_two(self):
        print('i did job two')
        self.notify('TWO')


class ComponentThree(AbstractComponent):
    def recive(self, reciver, message):
        print(f'recive {message} from {reciver}')

    def notify(self, message):
        self._mediator.notify(f'Hello')

    def do_job_three(self):
        print('i did job three')
        self.notify('THREE')


com_1 = ComponentOne()
com_2 = ComponentTwo()
com_3 = ComponentThree()

mediator_instance = MediatorOne(com_1, com_3)

com_1.do_job_one()
