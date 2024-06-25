from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner_name: str = None

    def set_owner(self, value: str):
        self._owner_name = value

    @abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def remove(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def display(self):
        pass


class ClickableItem(Item):
    def __init__(self, name: str):
        super().__init__(name)

    def remove(self, sub_item: 'Item'):
        raise Exception("You cant remove subitem")

    def display(self):
        print(self._owner_name + self._item_name)

    def add(self, sub_item: 'Item'):
        raise Exception("You cant add subitem")


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self._children = []

    def add(self, sub_item: 'Item'):
        sub_item.set_owner(self._item_name)
        self._children.append(sub_item)

    def remove(self, sub_item: 'Item'):
        self._children.remove(sub_item)

    def display(self):
        for i in self._children:
            if self._owner_name is not None:
                print(self._owner_name, end=" ")
            i.display()


def main():
    file = DropDownItem("file")
    create = DropDownItem("create")
    open_ = DropDownItem("open")
    exit_ = ClickableItem("exit")

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project = ClickableItem('Project')
    repository = ClickableItem('Repository')

    create.add(project)
    create.add(repository)

    file.display()


if __name__ == '__main__':
    main()


