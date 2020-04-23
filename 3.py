class Cell:
    def __init__(self, cell_count):
        self.count = cell_count

    def __add__(self, other):
        return self.count + other.count


    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.count - other.count
        return 'недопустимая операция'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        # TODO Zerosized
        return self.count // other.count

    def make_order(self, cell_in_row):
        res_str = ''
        res = divmod(self.count, cell_in_row)
        for i in range(res[0]):
            for j in range(cell_in_row):
                res_str += '*'
            res_str += '\n'
        if res[1] > 0:
            for i in range(res[1]):
                res_str += '*'
        return res_str


cell_1 = Cell(1)
cell_2 = Cell(2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
