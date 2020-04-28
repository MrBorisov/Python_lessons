class ComplexNumber:
    def __init__(self, a, b):
        self.complex = complex(a, b)

    def __add__(self, other):
        return {self.complex + other.complex}

    def __mul__(self, other):
        return self.complex * other.complex

    def __str__(self):
        return self.complex


num_1 = ComplexNumber(1, -2)
num_2 = ComplexNumber(3, 4)
print(num_1.complex)
print(num_1 + num_2)
print(num_1 * num_2)