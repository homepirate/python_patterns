from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass


class JapaneseEngine(IEngine):
    def release_engine(self):
        return f'{self.__class__.__name__}'


class RussianEngine(IEngine):
    def release_engine(self):
        return f'{self.__class__.__name__}'


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class JapaneseCar(ICar):
    def release_car(self, engine: IEngine):
        print(f"Make new {self.__class__.__name__} with {engine.release_engine()}")


class RussianCar(ICar):
    def release_car(self, engine: IEngine):
        print(f"Make new {self.__class__.__name__} with {engine.release_engine()}")


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):

    def create_engine(self) -> IEngine:
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):

    def create_engine(self) -> IEngine:
        return RussianEngine()

    def create_car(self) -> ICar:
        return RussianCar()


def main():
    ru_factory = RussianFactory()
    jp_factory = JapaneseFactory()
    factories = [ru_factory, jp_factory]

    for factory in factories:
        engine = factory.create_engine()
        car = factory.create_car()
        car.release_car(engine)


if __name__ == '__main__':
    main()
