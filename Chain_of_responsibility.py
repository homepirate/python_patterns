from abc import ABCMeta, abstractmethod


class IWorker(metaclass=ABCMeta):
    @abstractmethod
    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        pass


class AbsWorker(IWorker):
    def __init__(self):
        self.__next_worker: IWorker = None

    def set_next_worker(self, worker: IWorker) -> IWorker:
        self.__next_worker = worker
        return worker

    def execute(self, command: str) -> str:
        if self.__next_worker:
            return self.__next_worker.execute(command)
        return ''


class Designer(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'design house':
            return f'{self.__class__.__name__} do {command}'
        else:
            return super().execute(command)


class Carpenters(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'laying bricks':
            return f'{self.__class__.__name__} do {command}'
        else:
            return super().execute(command)


class FinishingWorker(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'interior decoration':
            return f'{self.__class__.__name__} do {command}'
        else:
            return super().execute(command)


def give_command(worker: IWorker, command: str):
    string: str = worker.execute(command)
    if not string:
        print(command + ' No one can do')
    else:
        print(string)


def main():
    designer = Designer()
    carpenters = Carpenters()
    finishing_worker = FinishingWorker()

    designer.set_next_worker(carpenters).set_next_worker(finishing_worker)

    give_command(designer, 'design house')
    give_command(designer, 'laying bricks')
    give_command(designer, 'interior decoration')
    give_command(designer, 'wait')


if __name__ == '__main__':
    main()
