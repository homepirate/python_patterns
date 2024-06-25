class ProviderCommunicate:
    def receive(self):
        print("Получение продукции от производителя")

    def payment(self):
        print("Оплата поставщику с удержанием комиссии")


class Site:
    def placement(self):
        print("Размещение на сайте")

    def delete(self):
        print("Удаление с сайта")


class Database:
    def insert(self):
        print("Добавлена запись в бд")

    def delete(self):
        print("Удаление из бд")


class Marketplace:

    def __init__(self):
        self.__provide_comm = ProviderCommunicate()
        self.__site = Site()
        self.__db = Database()

    def product_receipt(self):
        self.__provide_comm.receive()
        self.__db.insert()
        self.__site.placement()

    def product_release(self):
        self.__provide_comm.payment()
        self.__db.delete()
        self.__site.delete()


def main():
    market_place = Marketplace()
    market_place.product_receipt()
    print()
    market_place.product_release()


if __name__ == '__main__':
    main()