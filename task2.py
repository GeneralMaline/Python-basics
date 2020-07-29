class road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calcul(self):
        print(f'Требуемая масса асфальта: {self.length * self.width * 25 * 5 / 1000:.2f} т')

a = road(int(input("Введите длину дороги в метрах: ")), int(input("Введите ширину дороги в метрах: ")))
a.calcul()