from abc import ABC, abstractmethod


class Singleton(type):
    _isinstance = None
    def __call__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super().__call__(*args, **kwargs)
        return cls._isinstance


class MediaDownloader(ABC):  # Abstract Factory
    def __init__(self, link):
        self.link = link

    @abstractmethod
    def download_profile(self):
        pass


class Instagram(MediaDownloader, metaclass=Singleton):  # product
    def download_profile(self):
        return f'I download {self.link} profile successful'
