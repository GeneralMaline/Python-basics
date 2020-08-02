class matrix:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return '\n'.join('  '.join(str(i) for i in j) for j in self.a)

    def __add__(self, other):
        try:
            return matrix([[int(self.a[j][i]) + int(other.a[j][i]) for i in range(len(self.a[j]))] for j in range(len(self.a))])
        except IndexError:
            'Ошибка! Матрицы должны быть одноразмерные!'

matrix1 = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = matrix([[11, 21, 31], [41, 51, 61], [71, 81, 91]])

print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
