from math import factorial


def fact(a):
    yield factorial(a)


for el in fact(3):
    print(el)
