
class Div_by_zero(Exception):
    def __init__(self, txt):
        self.message = txt

inp_num = [1, 3, -2, 0, 50]

for el in inp_num:
    try:
        if el == 0:
            raise Div_by_zero("Деление на 0 не допустимо, хотя лично я считаю что зря, "
                              "должно получатся то число которое делим")
        out_date = 100 / el
    except Div_by_zero as err:
        print(err)
    else:
        print(out_date)
