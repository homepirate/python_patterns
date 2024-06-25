from abc import ABCMeta, abstractmethod


class IProcessor(metaclass=ABCMeta):

    @abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):

    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print(f"Data {self.__data}")


class Shell(IProcessor):
    def __init__(self, pr: IProcessor):
        self.processor = pr

    @abstractmethod
    def process(self):
        self.processor.process()


class HammingCoder(Shell):

    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print(f"code {self.__class__.__name__}", end=" ")
        self.processor.process()


class Encryptor(Shell):

    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print(f"Encrypt data ", end=" ")
        self.processor.process()


def main():
    transmitter = Transmitter('12345')
    transmitter.process()
    print()

    hamming_code = HammingCoder(transmitter)
    hamming_code.process()
    print()

    encr = Encryptor(hamming_code)
    encr.process()


if __name__ == '__main__':
    main()
