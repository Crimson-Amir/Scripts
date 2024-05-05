

class WaterContler:
    @staticmethod
    def turn_on():
        return 'water controller is on'


class WindowsController:
    @staticmethod
    def open_windows():
        return 'all windows is open now!'


class KeyController:
    @staticmethod
    def keys_on():
        return 'all keys is on!'


class CentralProcessor:
    def __init__(self):
        self.water = WaterContler()
        self.windows = WindowsController()
        self.keys = KeyController()

    def turn_on_everything(self):
        return self.water.turn_on(), self.windows.open_windows(), self.keys.keys_on()



def client():
    instance = CentralProcessor()
    result = instance.turn_on_everything()
    print(result)


client()



