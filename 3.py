def min_salary(list_of_workers):
    for worker in list_of_workers:
        try:
            if float(worker[1]) < 20000:
                print(f'{worker[0]} получает меньше 20000 рублей его зп = {worker[1]}')
        except ValueError:
            print('Некорректные данные')


def average_salary(list_of_workers):
    sum_salary = 0
    for worker in list_of_workers:
        try:
            sum_salary += float(worker[1])
        except ValueError:
            print('Некорректные данные')
    return sum_salary / len(list_of_workers)


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
