from typing import List, Dict


class Shared:

    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passwort = passport


    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passwort


class Flyweight:

    def __init__(self, shared: Shared):
        self.__shared = shared

    def get_data(self, unique: Unique):
        return f'{self.__shared.company}, {self.__shared.position}, {unique.name}, {unique.passport}'


class FlyweightFactory:

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = dict()
        for sh in shareds:
            self.__flyweights[self.get_key(sh)] = Flyweight(sh)

    def get_key(self, shared: Shared):
        return f'{shared.company}, {shared.position}'

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print("Не найден создаем новый")
            self.__flyweights[key] = Flyweight(shared)
        else:
            return self.__flyweights[key]

    def list_flyweights(self):
        count = len(self.__flyweights)
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_specialist_database(ff: FlyweightFactory, company: str, position: str, name: str, passport):
    flyweight = ff.get_flyweight(Shared(company, position))
