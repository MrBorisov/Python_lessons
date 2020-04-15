""""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\output_date_5.txt", 'w+') as file:
        file.write(input('введите строку чисел разделенных пробелами: '))
        file.seek(0)
        content = file.read()
        result = 0
    try:
        for el in content.split():
            result += int(el)
        print(f'сумма = {result}')
    except ValueError:
        print('Ошибка, надо вводить числа')
except IOError:
    print("Произошла ошибка ввода-вывода!")

