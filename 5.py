try:
    with open("task_5.txt", 'w+') as file:
        file.write(input('введите строку чисел разделенных пробелами: '))
        file.seek(0)
        content = file.read()
        result = 0
except IOError:
    print("Произошла ошибка ввода-вывода!")
try:
    for el in content.split():
        result += int(el)
    print(f'сумма = {result}')
except ValueError:
    print('Ошибка, надо вводить числа')
