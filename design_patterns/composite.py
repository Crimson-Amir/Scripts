from abc import ABC, abstractmethod


class Being(ABC):
    @abstractmethod
    def execute(self):
        pass


class AnimalLeaf(Being):
    def execute(self):
        return 'aniaml'


class Human(Being):
    def __init__(self):
        self._execute = []

    def add(self, name):
        self._execute.append(name)

    def execute(self):
        for exe in self._execute:
            exe.execute()


class Male:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name)


class Female:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name)



def client():
    f1 = Female('Mary')
    m1 = Male('Albert')

    h = Human()
    h.add(f1)
    h.add(m1)

    h.execute()


client()