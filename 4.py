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
    with open("task_4.txt", "w", encoding='utf-8') as file:
        for el in list:
            trans_word = translate(el[0])
            file.write(trans_word.title() + ' — ' + el[1] + '\n')
    print('Перевод записан')

list_of_words = []
try:
    with open("text_4.txt", encoding='utf-8') as file:
        for line in file:
            date = line.split()
            list_of_words.append(date[::2])
except IOError:
    print("Произошла ошибка ввода-вывода!")

output_date(list_of_words)
