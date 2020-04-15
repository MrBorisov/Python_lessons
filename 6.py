lessons = {}
with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\text_6.txt", encoding='utf-8') as file:
    data = file.read()

    """
    Для хранения положения в строке index - текущая позиция index_start - позиция для начала среза
    index_end - позиция для конца среза
    """
    index = 0
    index_start = 0
    index_line = 0
    while index_line != -1:
        index_line = data.find('\n', index_line + 1)
        sum_of_hour = 0
        i = data.find(':', index_start, index_line)
        if i != -1:
            index = i
            ls = data[index_start:index]
            lessons[ls] = ''
            while True:
                index_start = index
                i = data.find('(', index_start + 1, index_line)
                if i != -1:
                    index = i
                    sum_of_hour += int(data[index - 2:index].lstrip())
                else:
                    lessons[ls] = sum_of_hour
                    index = index_line
                    index_start = index_line + 1
                    break

print(lessons)
