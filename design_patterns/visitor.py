"""in fact, I don't undrstand this design pattern well"""
import abc


class PublicVehicle(abc.ABC):
    def __init__(self, dest):
        self.destenation = dest

    @abc.abstractmethod
    def order_ticket(self, visitor):
        pass


class Bus(PublicVehicle):
    def order_ticket(self, visitor):
        visitor.bus_ticket(self)


class Plane(PublicVehicle):
    def order_ticket(self, visitor):
        visitor.plane_ticket(self)


class Visitor:
    @staticmethod
    def bus_ticket(elemnt):
        print(f'bus ticket to {elemnt.destenation}')

    @staticmethod
    def plane_ticket(elemnt):
        print(f'plane ticket to {elemnt.destenation}')


a = Plane('mashhad')
visitor = Visitor()
a.order_ticket(visitor)