class _complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Результат сложения: ({self.a + other.a}+{self.b + other.b}j)'
    def __mul__(self, other):
        return f'Результат умножения: {complex(self.a, self.b) * complex(other.a, other.b)}'

x = _complex(2, 4)
y = _complex(1, -3)
print(x + y)
print(x * y)
