from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, emp: 'Employee', msg: str):
        pass


class Employee(metaclass=ABCMeta):
    def __init__(self, mediator: IMediator):
        self._mediator = mediator

    def set_mediator(self, value: IMediator):
        self._mediator = value


class Designer(Employee):

    def __init__(self, mediator: IMediator = None):
        super().__init__(mediator)
        self.__is_working = False

    def execute_work(self):
        print("Designer start working")
        self._mediator.notify(self, 'Designer design')

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print("Designer free")
        else:
            print("Designer working")


class Director(Employee):
    def __init__(self, mediator: IMediator = None):
        super().__init__(mediator)
        self.__text = None

    def give_command(self, txt: str):
        self.__text = txt
        if txt == '':
            print("Director know, what designer working")
        else:
            print(f"Director give command {txt}")
        self._mediator.notify(self, txt)


class Controller(IMediator):

    def __init__(self, designer: Designer, director: Director):
        super().__init__()
        self.__designer = designer
        self.__director = director

        self.__designer.set_mediator(self)
        self.__director.set_mediator(self)

    def notify(self, emp: 'Employee', msg: str):
        if isinstance(emp, Director):
            if msg == '':
                self.__designer.set_work(False)
            else:
                self.__designer.set_work(True)

        elif isinstance(emp, Designer):
            if msg == 'Designer design':
                self.__director.give_command('')


def main():
    designer = Designer()
    director = Director()

    mediator = Controller(designer, director)
    director.give_command("Design")
    print()
    designer.execute_work()


if __name__ == '__main__':
    main()
