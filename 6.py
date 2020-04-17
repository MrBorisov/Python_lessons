lessons = {}
"""
    Для хранения положения в строке index - текущая позиция index_start - позиция для начала среза
    index_end - позиция для конца среза
"""
with open("text_6.txt", encoding='utf-8') as file:
    for line in file:

        index_start = 0
        index_line = len(line)
        sum_of_hour = 0
        i = line.find(':', index_start, index_line)
        if i != -1:
            index = i
            ls = line[index_start:index]
            lessons[ls] = ''
            while True:
                index_start = index
                i = line.find('(', index_start + 1, index_line)
                if i != -1:
                    index = i
                    sum_of_hour += int(line[index - 2:index].lstrip())
                else:
                    lessons[ls] = sum_of_hour
                    break

print(lessons)
