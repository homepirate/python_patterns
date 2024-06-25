from abc import ABCMeta, abstractmethod


class IDateReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass


class DatabaseReader(IDateReader):
    def read(self):
        print("Data from db ", end=" ")


class FileReader(IDateReader):
    def read(self):
        print("Data from file", end=" ")


class Sender(metaclass=ABCMeta):
    def __init__(self, data_reader: IDateReader):
        self.reader: IDateReader = data_reader

    def set_data_reader(self, data_reader: IDateReader):
        self.reader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, data_reader: IDateReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print("Send by Email")


class TGBotSender(Sender):
    def __init__(self, data_reader: IDateReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print("Send by TelegramBot")


def main():
    sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TGBotSender(FileReader())
    sender.send()


if __name__ == '__main__':
    main()
