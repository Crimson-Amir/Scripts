from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    def execute(self):
        pass


class SimpleCommand(AbstractCommand):
    def __init__(self, number):
        self.number = number

    def execute(self):
        print(f'this is number -> {self.number}')


class ComplexCommand(AbstractCommand):
    def __init__(self, reciver, arg_1, arg_2):
        self.reciver = reciver
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def execute(self):
        print('this is so complex. i take care by reciver')
        self.reciver.do_job_one(self.arg_1)
        self.reciver.do_job_two(self.arg_2)


class Reciver:
    @staticmethod
    def do_job_one(arg):
        print(f'this is {arg}')

    @staticmethod
    def do_job_two(arg):
        print(f'this is {arg}')


class Invoker:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def operation(self):
        for key, value in self.__dict__.items():
            print(f'going to run {key}:', end='\n')
            value.execute()


job_one = SimpleCommand(5)
reciver = Reciver()
job_two = ComplexCommand(reciver, 1, 2)

invoker = Invoker(first_job=job_one, second_job=job_two)
invoker.operation()