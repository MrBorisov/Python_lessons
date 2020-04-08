def check_input(input_str):
    """
    Проверяем ввод от пользователя, должен содержать только латиницу
    :param input_str: строка от пользователя
    :return: True or False
    """
    leters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    input_str = ''.join(input_str.split())
    input_list = list(input_str.lower())
    for element in input_list:
        if element in leters:
            continue
        else:
            return False
    return True


def int_func(words):
    """
    Меняем первую букву на залавню, остальные делаем строчными
    :param words: строка от пользователя
    :return: Возвращаем все слова с большой буквы
    """
    return words.title()


def save_format(words):
    """
    Меняем первую букву на заглавную, остальные не трогаем
    Перебираем каждую букву из слова word
    Добавляем букву в список my_list
    после добавляем пробел, затем удаляем первую букву и заменяем ее на Заглавную
    (проверку не стал делать, подумал проще заменять даже заглавные чем еще 4 строки дописать)
    Затем конкатинируем строку result_string с полученным словом в my_list и возвращаем result_string
    с удалением пробелов в конце строки
    :param words: строка от пользователя
    :param result_string строка для хранения промежуточного результата
    :return: Возвращаем все слова с большой буквы, остальное форматирование сохраняем
    """
    result_string = ''
    """ Перебераем каждое слово из строки words"""
    for word in words.split():
        my_list = []

        for leter in word:
            my_list.append(leter)
        my_list.append(' ')
        my_list.pop(0)
        my_list.insert(0, word[0].upper())
        result_string = result_string + ''.join(my_list)
    return result_string.strip()

word = input('Введите слово маленькими латинскими буквами: ')
if check_input(word):
    print(f' Метод words.title() {int_func(word)}')
    print(f' Метод save_format {save_format(word)}')
else:
    print('Надо вводить слова ЛАТИНСКИМИ БУКВАМИ')
