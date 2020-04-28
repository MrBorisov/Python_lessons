
class Num_check(Exception):
    def __init__(self, txt):
        self.message = txt


res = []
is_go = True
while is_go:
    try:
        for i in input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split():
            if not i.isdigit():
                if i != '#':
                    raise Num_check("Вы ввели не число")
                else:
                    is_go = False

            else:
                res.append(int(i))
        print(res)
    except Num_check as err:
        print(err)

