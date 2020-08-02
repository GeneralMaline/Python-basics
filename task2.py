from abc import ABC, abstractmethod
class Clothes (ABC):
    @abstractmethod
    def palto (self):
        pass
    @abstractmethod
    def costum (self):
        pass
class Palto (Clothes):
    def __init__(self, V):
        self.V = V
    @property
    def palto(self):
        return f'Размер пальто: {self.V / 6.5 + 0.5:.2f}'

    def costum(self):
        pass


class Costum (Clothes):
    def __init__(self, H):
        self.H = H
    def palto (self):
        pass
    @property
    def costum(self):
        return f'Размер костюма: {2 * self.H + 0.3}'

a = Palto(int(input('Введите значение V для пальто ')))
print(a.palto)

b = Costum(int(input('Введите значение H для костюма ')))
print(b.costum)