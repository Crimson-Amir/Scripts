import abc
import json

user, password = 'amir', 1383
json_file = '{"first_one": "OK"}'


class Page(abc.ABC):
    @abc.abstractmethod
    def show(self):
        pass


class AnnoPage(Page):
    def show(self):
        return 'ok'

    @staticmethod
    def return_dict(dict_):
        return dict_['first_one']


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


class Adapter:
    @staticmethod
    def json_to_dict(json_data):
        return json.loads(json_data)


a = AuthPage()
b = Decorator(a)

c = AnnoPage()
adapter = Adapter()
c = c.return_dict(adapter.json_to_dict(json_file))

print(c)