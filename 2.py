from abc import ABC, abstractmethod


class clothes(ABC):
    @abstractmethod
    def consumpt(self):
        pass


class Coat:
    def __init__(self, size):
        self.size = size

    @property
    def consumpt(self):
        res = round(self.size / 6.5 + 0.5, 2)
        return res


class Costume:
    def __init__(self, height):
        self.height = height

    @property
    def consumpt(self):
        res = round(2 * self.height + 0.3, 3)
        return res


my_coat = Coat(48)
print(my_coat.consumpt)
my_costume = Costume(2.2)
print(my_costume.consumpt)
