from abc import ABCMeta, abstractmethod


class Reader(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader

    def read(self, url: str):
        self.__reader.parse(url)


class NewsSiteReader(Reader):
    def parse(self, url: str):
        print(f"Parsing news site {url}")


class SocialNetworkReader(Reader):
    def parse(self, url: str):
        print(f"Parsing social network {url}")


class TelegramChannelReader(Reader):
    def parse(self, url: str):
        print(f"Parsing telegram channel {url}")


def main():
    resource_reader = ResourceReader(NewsSiteReader())
    url ='http://news.ru'
    resource_reader.read(url)

    url = 'http://vk.ru'
    resource_reader.set_strategy(SocialNetworkReader())
    resource_reader.read(url)

    url = '@tg_channel'
    resource_reader.set_strategy(TelegramChannelReader())
    resource_reader.read(url)


if __name__ == '__main__':
    main()

