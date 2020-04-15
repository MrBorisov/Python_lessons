"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator


def translate(word: str):
    """
    Через гугл API делаем перевод word с английского на русский
    :param word: строка
    :return: строка
    """
    translator = Translator()
    result = translator.translate(word, src='en', dest='ru')
    return (result.text)

def output_date(list):
    with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\output_date.txt", "w") as file:

        for el in list:
            trans_word = translate(el[0])
            file.write(trans_word.title() + ' — ' + el[1] + '\n')

list_of_words = []
try:
    with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\text_4.txt", encoding='utf-8') as file:
        for line in file:
            date = line.split()
            list_of_words.append(date[::2])
        print(list_of_words)
except IOError:
    print("Произошла ошибка ввода-вывода!")

output_date(list_of_words)