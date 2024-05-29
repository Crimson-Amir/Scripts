import datetime
from random import sample
from string import ascii_letters


class Originator:
    final_result = None

    def __init__(self, res):
        self.final_result = res
        print(f'Originator: initialaize Originator -> {self.final_result}')

    def chenge_result(self):
        self.final_result = ''.join(sample(ascii_letters ,10))
        print(f'Originator: result changed -> {self.final_result}')

    def save(self):
        return SaveMemento(self.final_result)

    def restore(self, memento):
        self.final_result = memento.get_state()
        print(f'Originator: result change back to -> {memento.get_state()}')


class SaveMemento:
    def __init__(self, state):
        self.state = state
        self.date = datetime.datetime.now()

    def get_state(self):
        return self.state

    def get_name(self):
        return f'{self.state} - {self.date}'


class CareTaker:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create_backup(self):
        self._mementos.append(self._originator.save())

    def print_s(self):
        print(self._originator.final_result)

    def undo(self):
        if not self._mementos:
            return None
        return self._originator.restore(self._mementos.pop())


originator_instance = Originator('hello')
caretaker = CareTaker(originator_instance)
caretaker.create_backup()
originator_instance.chenge_result()
caretaker.create_backup()
originator_instance.chenge_result()
caretaker.create_backup()


caretaker.undo()
caretaker.undo()
caretaker.undo()

