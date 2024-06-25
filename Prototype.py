import copy


class Sheep:

    __name: str = ''
    __params: dict = {'Weight': 30, 'Growth': 0.3}

    def __init__(self, donor: 'Sheep' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def get_params(self):
        return self.__params

    def set_weight(self, value):
        self.__params['Weight'] = value

    def clone(self):
        return Sheep(self)


def main():
    sheep_donor = Sheep()
    sheep_donor.set_name("Dolli")

    sheep_clone = sheep_donor.clone()
    print(sheep_donor.get_name(), sheep_donor.get_params())
    print(sheep_clone.get_name(), sheep_clone.get_params())

    sheep_clone.set_name('New')
    sheep_clone.set_weight(50)
    print()

    print(sheep_donor.get_name(), sheep_donor.get_params())
    print(sheep_clone.get_name(), sheep_clone.get_params())


if __name__ == '__main__':
    main()
