from abc import ABCMeta, abstractmethod
from typing import List, Deque


class ICommand(metaclass=ABCMeta):
    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass


class Conveyor:

    def on(self):
        print('Conveyor start')

    def off(self):
        print('Conveyor stop')

    def speed_incr(self):
        print('Speed up')

    def speed_decr(self):
        print('Speed down')


class ConveyerWorkCommand(ICommand):
    def __init__(self, conveyer: Conveyor):
        self.conveyer = conveyer

    def positive(self):
        self.conveyer.on()

    def negative(self):
        self.conveyer.off()


class ConveyorAdjustCommand(ICommand):
    def __init__(self, conveyer: Conveyor):
        self.conveyer = conveyer

    def positive(self):
        self.conveyer.speed_incr()

    def negative(self):
        self.conveyer.speed_decr()


class Multipult:
    def __init__(self):
        self.__comands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__comands[button] = command

    def press_on(self, button: int):
        self.__comands[button].positive()
        self.__history.append(self.__comands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


def main():
    conveyor = Conveyor()
    multipult = Multipult()
    multipult.set_command(0, ConveyerWorkCommand(conveyor))
    multipult.set_command(1, ConveyorAdjustCommand(conveyor))

    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()


if __name__ == '__main__':
    main()
