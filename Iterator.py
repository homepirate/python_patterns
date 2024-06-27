import copy


class DataStack:
    def __init__(self, my_stack: 'DataStack' = None):
        self.__items = [0] * 10
        self.__length = 0

        if my_stack:
            self.__items = copy.deepcopy(my_stack.__items)
            self.__length = my_stack.__length

    @property
    def items(self):
        return self.__items

    @property
    def length(self):
        return self.__length

    def push(self, item):
        self.__items[self.__length] = item
        self.__length += 1

    def pop(self):
        self.__length -= 1
        return self.__items[self.__length]

    def __eq__(self, other: 'DataStack'):
        it1, it2 = StackIterator(self), StackIterator(other)

        while not it1.is_end() or not it2.is_end():
            if next(it1) != next(it2):
                break
        return it1.is_end() and it2.is_end()


class StackIterator:

    def __init__(self, my_stack: DataStack):
        self.__stack = my_stack
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_index = self.__index
        self.__index += 1

        if current_index < self.__stack.length:
            return self.__stack.items[current_index]
        return 0

    def is_end(self) -> bool:
        return self.__index == self.__stack.length + 1


def main():
    stack1 = DataStack()
    for i in range(1, 5):
        stack1.push(i)

    stack2 = DataStack(stack1)

    print(stack1 == stack2)
    print(stack1.items)
    print(stack1.pop())
    print(stack1 == stack2)


if __name__ == '__main__':
    main()
