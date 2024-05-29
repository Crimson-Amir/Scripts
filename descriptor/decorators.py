


class Person:
    def __init__(self, name, car):
        self._name = name
        self.car = car

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError
        self._name = value

    @name.deleter
    def name(self):
        self._name = None

    def __get__(self, instance, owner):
        pass

a = Person('amir')
a.name = 'ali'
del a.name
print(a.name)