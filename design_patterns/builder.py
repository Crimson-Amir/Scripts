import abc


class DisruptionRadar:
    def __init__(self):
        self._isp = None
        self._date = None
        self._statistics = None

    def set_isp(self, isp):
        self._isp = isp

    def set_date(self, date):
        self._date = date

    def set_statistics(self, statistics):
        self._statistics = statistics

    def return_clean_data(self):
        return f'{self._isp} {self._date.date} {self._statistics.statistics}'


class AbstractBuilder(abc.ABC):
    @abc.abstractmethod
    def request(self): pass

    @abc.abstractmethod
    def get_isp_name(self): pass

    @abc.abstractmethod
    def get_date(self): pass

    @abc.abstractmethod
    def get_and_sort_statistics(self): pass


class ConcreteWikipedia(AbstractBuilder):
    def request(self):
        instance = Reuest()
        instance.url = 'url'
        return instance

    def get_isp_name(self):
        return self.__class__.__name__

    def get_date(self):
        instace = DateInfo()
        instace.date = 'Now'
        return instace

    def get_and_sort_statistics(self):
        instance = Statistics()
        instance.statistics = 'None'
        return instance


class ConcreteGithub(AbstractBuilder):
    def request(self):
        instance = Reuest()
        instance.url = 'url'
        return instance

    def get_isp_name(self):
        return self.__class__.__name__

    def get_date(self):
        instace = DateInfo()
        instace.date = 'Now'
        return instace

    def get_and_sort_statistics(self):
        instance = Statistics()
        instance.statistics = 'None'
        return instance


class Director:
    _builder : ConcreteGithub = None

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        radar = DisruptionRadar()

        radar.set_isp(self._builder.get_isp_name())
        radar.set_date(self._builder.get_date())
        radar.set_statistics(self._builder.get_and_sort_statistics())

        return radar


class Reuest: url = None
class DateInfo: date = None
class Statistics: statistics = None


def client_builder(target):
    targets = {
        'wikipedia': ConcreteWikipedia,
        'github': ConcreteGithub
    }

    app = targets[target]()
    director = Director(app)
    construct = director.construct()
    return construct.return_clean_data()


print(client_builder('wikipedia'))