a = int(input('введите результат первого дня: '))
b = int(input('введите цель: '))
day = 1
while a < b:
    a = a + a * 10 / 100
    day += 1
print(day)