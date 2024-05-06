from abc import ABC, abstractmethod


class Elevator:
    _state = None

    def __init__(self, state):
        self.set_state(state)

    def set_state(self, state):
        self._state = state
        self._state.set_elevator(self)

    def show_state(self):
        print(self._state.__class__.__name__)

    def state_up(self):
        self._state.state_up_btn()

    def state_down(self):
        self._state.state_down_btn()


class State(ABC):
    _elevetor = None

    def set_elevator(self, elevetor):
        self._elevetor = elevetor


    @abstractmethod
    def state_up_btn(self):
        pass

    @abstractmethod
    def state_down_btn(self):
        pass


class FirstFloor(State):
    def state_up_btn(self):
        print('1 more up')
        self._elevetor.set_state(SecondFloor())

    def state_down_btn(self):
        print('there is no down floor exist')


class SecondFloor(State):
    def state_up_btn(self):
        print('1 more up')
        self._elevetor.set_state(ThirdFloor())

    def state_down_btn(self):
        print('1 more down')
        self._elevetor.set_state(FirstFloor())


class ThirdFloor(State):
    def state_up_btn(self):
        print('there is no up exist')

    def state_down_btn(self):
        print('1 more down')
        self._elevetor.set_state(SecondFloor())


elavetor = Elevator(FirstFloor())
elavetor.show_state()
elavetor.state_up()
elavetor.show_state()
elavetor.state_down()
elavetor.show_state()
