from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self) -> float:
        pass

    @abstractmethod
    def adjust(self):
        pass


class RussianScales(IScale):

    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight

    def adjust(self):
        print("Adjustment " + self.__class__.__name__)


class BritishScales:

    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight

    def adjust(self):
        print("Adjustment " + self.__class__.__name__, end=" ")


class AdapterForBritishScales(BritishScales, IScale):
    def __init__(self, cw: float):
        super().__init__(cw)
        
    def get_weight(self) -> float:
        return super().get_weight() * 0.453
    
    def adjust(self):
        super().adjust()
        print("adapter")


def main():
    kg = 55.
    lb = 55.

    rScales = RussianScales(kg)
    bScales = AdapterForBritishScales(lb)

    print(rScales.get_weight())
    rScales.adjust()
    print(bScales.get_weight())
    bScales.adjust()


if __name__ == '__main__':
    main()
