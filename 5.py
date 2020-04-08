def check_input(input_list):
    """
    Проверка ввода пользователя, на вход получаем список элементов, проверяем что бы там были только цифры и q в конце
    или просто q. True если ввод корректен и False если не корректен
    :param input_list: список от введенной строки
    :return: True or False
    """
    if input_list[-1] == '$':
        input_list = input_list[:-1]
    for element in input_list:
        try:
            int(element)
        except ValueError:
            return False
    else:
        return True


def sum_of_elements(list_of_el):
    """
    Суммирует все элементы списка поданного на вход. На вход получаем список чисел в текстовом формате, возвращаем
    сумму этих чисел + сумма предыдущих вычислений, записанная в global result
    :param list_of_el: Список из строк содержащих числа
    :return: сумму int в переменной result
    """
    global result
    for element in list_of_el:
        result = result + int(element)
    return result


result = 0
is_stop = True
"""Основной цикл остановится если пользователь введет $"""
while is_stop:
    list_of_elements = input('Введите числа через пробел, если хотите закончить введите $ в конце '
                             'или просто $: ').split()
    """Сначала проверим ввод"""
    if check_input(list_of_elements):
        if list_of_elements[-1] == '$':
            print(f' Итоговая сумма = {sum_of_elements(list_of_elements[:-1])}')
            is_stop = False
        else:
            print(sum_of_elements(list_of_elements))
    else:
        print('вы ввели не привильную строку. необходимо ввести числа через пробел и q в конце строки или просто $')
