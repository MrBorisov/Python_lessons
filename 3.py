"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
 методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить
 работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
 вызвать методы экземпляров).
"""
from builtins import print


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        if self.position == "Batman":
            print(f'Total income = infinity')
            print('Because he is Batman')
        else:
            t_inkom = self._income.get('wage') + self._income.get('bonus')
            print(f'ЗП + премия = {t_inkom}')


w = Position('Bruce', 'Wayne', 'Batman', 1000, 100)
print(w.position)
w.get_full_name()
w.get_total_income()

s = Position('Jerry', 'Smith', 'manager', 100, 10)
print(s.position)
s.get_full_name()
s.get_total_income()
