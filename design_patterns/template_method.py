from abc import ABC, abstractmethod

class Super(ABC):
    def template_method(self):
        self.step_1()
        self.step_2()
        self.step_3()
        self.step_4()

    @staticmethod
    def step_1():
        print('this is step 1')

    @staticmethod
    def step_2():
        print('this is step 2')

    @abstractmethod
    def step_3(self):
        print('this is step 3')

    @abstractmethod
    def step_4(self):
        print('this is step 4')



class One(Super):
    def step_3(self):
        print('no this is not step 3')

    def step_4(self):
        print('no this is not step 4')



One().template_method()