from random import randint


def auto_test():
    """
    Тестируем две функции возведения в степень exponentiation и exponent_vithout
    :return: возвращаем true и значения елси они совпадают и false и значения если не совпадают
    """
    list_of_x = []
    list_of_y = []
    for i in range(5):
        list_of_x.append(randint(1, 15))
        list_of_y.append(randint(1, 10) * -1)
    for x in list_of_x:
        for y in list_of_y:
            res_a = exponentiation(x, y)
            res_b = exponent_vithout(x, y)
            if res_a == res_b:
                print(f'True {res_a} = {res_b} x = {x} y = {y}')
            else:
                print(f'False {x} {y}')


def exponentiation(x, y):
    """
    Возводит x в степень y
    :param x: float
    :param y: float отрицательное число
    :return: x в степени y
    """
    return round(x ** y, 12)


def exponent_vithout(x, y):
    """
    Возводит x в степень y
    :param x: float
    :param y: float отрицательное число
    :return: x в степени y
    """

    result = 1
    list = []
    for i in range(abs(y)):
        list.append(x)
    for i in list:
        result = result * i
    return round(1 / result, 12)


auto_test()
