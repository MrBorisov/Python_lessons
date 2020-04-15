"""Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def min_salary(list_of_workers):
    for worker in list_of_workers:
        if float(worker[1]) < 20000:
            print(f'{worker[0]} получает меньше 20000 рублей его зп = {worker[1]}')


def average_salary(list_of_workers):
    sum = 0
    for worker in list_of_workers:
        sum += float(worker[1])
    return sum / len(list_of_workers)


list_of_workers = []
try:
    with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\text_3.txt", encoding='utf-8') as file:
        for line in file:
            date = line.split()
            list_of_workers.append(date)
        print(list_of_workers)
except IOError:
    print("Произошла ошибка ввода-вывода!")

min_salary(list_of_workers)
print(f'Средняя зарплата = {average_salary(list_of_workers)}')
