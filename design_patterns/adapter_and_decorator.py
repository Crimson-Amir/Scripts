import abc


user, password = 'amir', 1383

class Page(abc.ABC):
    @abc.abstractmethod
    def show(self):
        pass


class AnnoPage(Page):
    def show(self):
        return 'ok'


class AuthPage(Page):
    def show(self):
        return 'ok'


class AbstractDecorator(Page, abc.ABC):
    def __init__(self, component):
        self._component = component

    def show(self):
        pass


class Decorator(AbstractDecorator):
    def show(self):
        if user == 'amir' and password == 1383:
            return self._component.show()
        else:
            print('wrong')


a = AuthPage()
b = Decorator(a)
print(b.show())