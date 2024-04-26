from abc import ABC, abstractmethod

class Singleton(type):
    _isinstance = None
    def __call__(self, *args, **kwargs):
        if not self._isinstance:
            self._isinstance = super().__call__(*args, **kwargs)
        return self._isinstance


class MediaDownloader(ABC):  # creator
    def __init__(self, link):
        self.link = link

    @abstractmethod
    def download_profile(self):
        pass


class Instagram(MediaDownloader, metaclass=Singleton):  # product
    def download_profile(self):
        return f'I download {self.link} profile successful'


class Twitter(MediaDownloader, metaclass=Singleton):
    def download_profile(self):
        return f'I download {self.link} profile successful'


class Linkdin(MediaDownloader, metaclass=Singleton):
    def download_profile(self):
        return f'I download {self.link} profile successful'


class Snapchat(MediaDownloader, metaclass=Singleton):
    def download_profile(self):
        return f'I download {self.link} profile successful'


def client(platform, link):  # client

    platform_class = {
        'instagram': Instagram,
        'twitter': Twitter,
        'linkdin': Linkdin,
        'snapchat': Snapchat
    }

    instance = platform_class[platform](link)
    return instance