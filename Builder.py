from abc import ABCMeta, abstractmethod

class Phone:
    def __init__(self):
        self.data: str = ''

    def about_phone(self) -> str:
        return self.data

    def append_data(self, value: str):
        self.data += value


class IDeveloper(metaclass=ABCMeta):

    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(IDeveloper):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Add Display AMOLED\n")

    def create_box(self):
        self.__phone.append_data("Add Box Titan\n")

    def system_install(self):
        self.__phone.append_data("Install OS Android\n")

    def get_phone(self) -> Phone:
        return self.__phone


class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Add Display AMOLED\n")

    def create_box(self):
        self.__phone.append_data("Add Box Metal\n")

    def system_install(self):
        self.__phone.append_data("Install OS IOS\n")

    def get_phone(self) -> Phone:
        return self.__phone


class Director:
    def __init__(self, developer: IDeveloper):
        self.__developer = developer

    def set_developer(self, developer: IDeveloper):
        self.__developer = developer

    def mount_phone(self) -> Phone:
        self.__developer.create_display()
        self.__developer.create_box()
        return self.__developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__developer.create_display()
        self.__developer.create_box()
        self.__developer.system_install()
        return self.__developer.get_phone()


def main():
    a_dev = AndroidDeveloper()
    i_dev = IphoneDeveloper()

    director = Director(a_dev)
    a_phone = director.mount_phone()
    print(a_phone.about_phone())

    director.set_developer(i_dev)
    i_phone = director.mount_full_phone()
    print(i_phone.about_phone())


if __name__ == '__main__':
    main()
