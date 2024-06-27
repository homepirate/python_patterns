from abc import ABCMeta, abstractmethod
from typing import List


class IVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, place: 'IPlace'):
        pass


class IPlace(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


class Zoo(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Cinema(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Circus(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class HolidayMaker(IVisitor):

    def __init__(self):
        self.value = ''

    def visit(self, place: 'IPlace'):
        if isinstance(place, Zoo):
            self.value = 'Elephant'
        elif isinstance(place, Cinema):
            self.value = 'Brother 2'
        elif isinstance(place, Circus):
            self.value = 'Clown'


def main():
    places: List[IPlace] = [Zoo(), Cinema(), Circus()]
    visitor = HolidayMaker()

    for p in places:
        p.accept(visitor)
        print(visitor.value)


if __name__ == '__main__':
    main()
