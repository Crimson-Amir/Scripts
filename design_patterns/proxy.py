import datetime
from abc import ABC, abstractmethod


class DataBaseManagerAbstract(ABC):
    @abstractmethod
    def insert(self):
        pass


class DataBaseManager(DataBaseManagerAbstract):
    def insert(self):
        return 'data inserted on db'


class DataBaseProxy(DataBaseManagerAbstract):
    def __init__(self, db_object):
        self.db_object = db_object

    @staticmethod
    def logging():
        print(f'user requests in {datetime.datetime.now()}')

    @staticmethod
    def end_of_requests():
        print(f'request is ended')

    def insert(self):
        self.logging()
        get_data = self.db_object.insert()
        self.end_of_requests()
        return get_data



db_manager = DataBaseManager()
proxy = DataBaseProxy(db_manager)
print(proxy.insert())

