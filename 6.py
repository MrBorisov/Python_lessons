a = int(input('введите результат первого дня: '))
b = int(input('введите цель: '))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
print(day)