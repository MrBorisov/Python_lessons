try:
    with open("task_2.txt") as file:
        num_of_str = 0
        num_of_words = 0
        for line in file:
            num_of_str += 1
            print(f' В {num_of_str} строке {len(line.split())} слов')
            num_of_words += len(line.split())
        print(f'Всего строк {num_of_str}, а слов {num_of_words}')
except IOError:
    print("Произошла ошибка ввода-вывода!")
