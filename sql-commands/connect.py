from psycopg2 import pool


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]


class Connect(metaclass=Singleton):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def connect(self):
        return pool.SimpleConnectionPool(1, 10, **self.__dict__)


def connect_client():
    return Connect(database="my_shop",
                   host="localhost",
                   user="postgres",
                   password="amir1383amir",
                   port=2053).connect()
