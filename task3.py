class worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class position(worker):
    def get_name(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        print(f'{position} {name} {surname}')
    def get_income(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        #self._income = {'wage': wage, 'bonus': bonus}
        print(self._income)


a = position("Вуди", 'Харрельсон', 'актёр', 10000, 3000)
a.get_name("Вуди", 'Харрельсон', 'актёр', 10000, 3000)
a.get_income("Вуди", 'Харрельсон', 'актёр', 10000, 3000)

b = position('Квентин', 'Тарантино', 'режиссёр', 20000, 6000)
b.get_name('Квентин', 'Тарантино', 'режиссёр', 20000, 6000)
b.get_income('Квентин', 'Тарантино', 'режиссёр', 20000, 6000)

# Ну бред какой-то получился, почему каждый раз нужно писать параметры в скобочках?