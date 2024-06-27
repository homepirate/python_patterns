from abc import ABCMeta, abstractmethod
from typing import List


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, value: int):
        pass


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def add_observer(self, o: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):

    def __init__(self, p: int):
        self.__price = p
        self.__observers: List[IObserver] = []

    def add_observer(self, o: IObserver):
        self.__observers.append(o)

    def remove_observer(self, o: IObserver):
        self.__observers.remove(o)

    def notify(self):
        for o in self.__observers:
            o.update(self.__price)

    def change_price(self, price: int):
        self.__price = price
        self.notify()


class Wholesale(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        self.__product.add_observer(self)

    def update(self, value: int):
        if value < 300:
            print(f"Wholesale Buy by price {value}")
            self.__product.remove_observer(self)


class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        self.__product.add_observer(self)

    def update(self, value: int):
        if value < 350:
            print(f"Buyer Buy by price {value}")
            self.__product.remove_observer(self)


def main():
    product = Product(400)
    wholesale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(320)
    product.change_price(280)


if __name__ == '__main__':
    main()
