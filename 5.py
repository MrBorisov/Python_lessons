my_list = [7, 5, 3, 3, 2]
while True:
    num = int(input('Введите целое положительное число: '))
    for el in my_list:
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