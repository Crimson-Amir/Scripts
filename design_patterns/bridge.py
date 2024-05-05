"""for cartesian product"""

from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def create(self):
        pass


class Keyboard(AbstractProduct):
    def create(self):
        return self._color.paint(self.__class__.__name__)


class AbstractColor(ABC):
    @abstractmethod
    def paint(self, product):
        pass


class Red(AbstractColor):
    def paint(self, product):
        return f'this is a {self.__class__.__name__} {product}'


def client(shape, color):
    color_name : AbstractColor = color()
    shape_class : AbstractProduct = shape(color_name)
    return shape_class.create()


print(client(Keyboard, Red))