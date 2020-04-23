"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

"""
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
