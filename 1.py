try:
    with open("task_1.txt", "a") as file:
        while True:
            data = input('Введите строку, для завершения не вводите ни чего :')
            if data:
                #file.write(data + '\n')
                print(data, file=file)
            else:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
