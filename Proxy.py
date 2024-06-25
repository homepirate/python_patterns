from abc import ABCMeta, abstractmethod
from typing import Dict


class ISite(metaclass=ABCMeta):

    @abstractmethod
    def get_page(self, num: int) -> str:
        pass


class Site(ISite):

    def get_page(self, num: int) -> str:
        return f"Page number {num}"


class SiteProxy(ISite):

    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = dict()

    def get_page(self, num: int) -> str:
        if self.__cache.get(num) is not None:
            page = "FROM cache " + self.__cache[num]
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page


def main():
    my_site: ISite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(1))


if __name__ == '__main__':
    main()
