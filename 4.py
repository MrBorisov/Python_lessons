number = int(input('Input number: '))
max_naumber = 0

while number > 0:
    n = number % 10
    if n == 9:
        max_naumber = n
        break
    elif n > max_naumber:
        max_naumber = n
        number = number // 10
    else:
        number = number // 10

print(max_naumber)