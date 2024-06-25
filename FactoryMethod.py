class IProduct:
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print(f"Make new {self.__class__.__name__}")


class Truck(IProduct):
    def release(self):
        print(f"Make new {self.__class__.__name__}")


class IWorkShop:
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self):
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self):
        return Truck()


def main():
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()


if __name__ == '__main__':
    main()
