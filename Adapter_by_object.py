from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self) -> float:
        pass


class RussianScales(IScale):

    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class BritishScales:

    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class AdapterForBritishScales(IScale):
    def __init__(self, br_scales: BritishScales):
        self.__british_scales = br_scales

    def get_weight(self) -> float:
        return self.__british_scales.get_weight() * 0.453


def main():
    kg = 55.
    lb = 55.

    rScales = RussianScales(kg)
    bScales = AdapterForBritishScales(BritishScales(lb))

    print(rScales.get_weight())
    print(bScales.get_weight())


if __name__ == '__main__':
    main()



