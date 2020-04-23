class Matrix:
    def __init__(self, matr):
        self.res_add = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.value_matrix = matr

    def __add__(self, other):
        for i in range(len(self.value_matrix)):

            for j in range(len(self.value_matrix[0])):
                self.res_add[i][j] = self.value_matrix[i][j] + other.value_matrix[i][j]
        res_string = ''
        for line in self.res_add:
            res_string += f'{line[0]} {line[1]} {line[2]}\n'
        return res_string

    def __str__(self):
        res_string = ''
        for line in self.value_matrix:
            res_string += f'{line[0]} {line[1]} {line[2]}\n'
        return res_string


my_m_1 = Matrix([[1, 3, 1], [2, 2, 2], [3, 2, 1]])
my_m_2 = Matrix([[1, 2, 1], [1, 1, 3], [1, 2, 2]])

print(my_m_1 + my_m_2)
print(my_m_1)
print(my_m_2)
