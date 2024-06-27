from abc import ABCMeta, abstractmethod
from typing import Deque


class IMemento(metaclass=ABCMeta):
    @abstractmethod
    def get_dollars(self) -> int:
        pass

    def get_euro(self) -> int:
        pass


class ExchangeMemento(IMemento):

    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self) -> int:
        return self.__dollars

    def get_euro(self) -> int:
        return self.__euro


class Exchange:

    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self):
        print(f"Dollars {self.__dollars}")

    def get_euro(self):
        print(f"Euro {self.__euro}")

    def sell(self):
        if self.__dollars > 0:
            self.__dollars -= 1

    def buy(self):
        self.__euro += 1

    def save(self) -> ExchangeMemento:
        return ExchangeMemento(self.__dollars, self.__euro)

    def restore(self, ex_m: IMemento):
        self.__dollars = ex_m.get_dollars()
        self.__euro = ex_m.get_euro()


class Memory:
    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history: Deque[IMemento] = []

    def backup(self):
        self.__history.append(self.__exchange.save())

    def undo(self):
        if len(self.__history) == 0:
            return
        self.__exchange.restore(self.__history.pop())


def main():
    exchange = Exchange(10, 10)

    memory = Memory(exchange)
    exchange.get_dollars()
    exchange.get_euro()

    print("SELL DOLLAR BUY EURO")
    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print("SAVE")
    memory.backup()

    print("SELL DOLLAR BUY EURO")

    exchange.sell()
    exchange.buy()

    exchange.get_dollars()
    exchange.get_euro()

    print("BACKUP")

    memory.undo()

    exchange.get_dollars()
    exchange.get_euro()


if __name__ == '__main__':
    main()