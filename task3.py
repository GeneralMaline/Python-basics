class cell():
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell >= other.cell:
            return cell(self.cell - other.cell)
        else:
            return 'Первое число должно быть больше второго!'

    def __mul__(self, other):
        return cell(self.cell * other.cell)

    def __truediv__(self, other):
        if self.cell % other.cell == 0:
            return cell(self.cell / other.cell)
        else:
            return 'Результатом деления должно быть целое число!'

    def __str__(self):
        return f'{self.cell}'

    def make_order(self, row):
        while self.cell >= row:
            print('* ' * row)
            self.cell = self.cell - row
        print('* ' * (self.cell % row))

a = cell(int(input('Введите значение для клетки 1 ')))

b = cell(int(input('Введите значение для клетки 2 ')))

print(a + b)

print(a - b)

print(a * b)

print(a / b)

a.make_order(int(input('Введите число столбцов для клетки 1: ')))