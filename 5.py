my_list = [7, 5, 3, 3, 2]
while True:
    while True:
        num = int(input('Введите целое положительное число: '))
        if num > 0:
            break
        else:
            print('Вы ввели не верное число!')
    for el in my_list:
        # Для оптимальности проверим на самое маленькое число
        if num <= my_list[-1]:
            my_list.append(num)
            break
        if num > el:
            index = my_list.index(el)
            my_list.insert(index, num)
            break
    print(my_list)
    finish = input('Для завершения введите q: ')
    if finish == 'q':
        break