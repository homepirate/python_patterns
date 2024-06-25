class DatabaseHelper:
    instance = None
    __data: str = None
    IP = None
    PORT = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, ip: str, port: int):
        if self.IP is None and self.PORT is None:
            self.IP = ip
            self.PORT = port

    def select_data(self):
        return self.__data

    def insert_data(self, value: str):
        self.__data = value


def main():
    db = DatabaseHelper('localhost', 8000)
    print(db.IP, db.PORT)
    db2 = DatabaseHelper('127.0.0.1', 8080)
    print(db2.IP, db2.PORT)
    print(db is db2)


if __name__ == '__main__':
    main()

