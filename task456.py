class sklad:
    stock = {'scanner': 50, 'printer': 80, 'xerox': 30}
    def __init__(self):
        print(f'Баланс склада: {self.stock}')
    def postuplenie(self, income):
        for i in self.stock:
            self.stock[i] += income[i]
        print(f'Остаток на складе: {self.stock}')

    def spisanie(self, transfer):
        for i in self.stock:
            if self.stock[i] > transfer[i]:
                self.stock[i] = self.stock[i] - transfer[i]
            else:
                print(f'Невозможно списать это количество {i}, будет списано {self.stock[i]} {i}')
                self.stock[i] = 0
        print(f'Остаток на складе: {self.stock}')


class orgtech:
    def __init__(self, proizvoditel, stoimost):
        self.proizvoditel = proizvoditel
        self.stoimost = stoimost
    def orgteh(self):
        print('postupaet na sklad')

class scanner(orgtech):
    def skan(self):
        print(f'В наличии сканеры {self.proizvoditel} за {self.stoimost}')

class printer(orgtech):
    def pechat(self):
        print(f'В наличии принтеры {self.proizvoditel} за {self.stoimost}')

class xerox(orgtech):
    def kopy(self):
        print(f'В наличии ксероксы {self.proizvoditel} за {self.stoimost}')

a = scanner('HP', 10000)
a.skan()

b = printer('Canon', 15000)
b.pechat()

c = xerox('Xerox', 5000)
c.kopy()

x = sklad()
try:
    if input('Хотите ли Вы отправить на склад технику? Вводите +, если да, или -, если нет ') == "+":
        x.postuplenie({'scanner': int(input('Кол-во поступаемых сканеров: ')), 'printer': int(input('Кол-во поступаемых принтеров: ')), 'xerox': int(input('Кол-во поступаемых ксероксов: '))})
    if input('Хотите ли Вы списать со склада технику? Вводите +, если да, или -, если нет ') == "+":
        x.spisanie({'scanner': int(input('Кол-во передаваемых сканеров: ')), 'printer': int(inpu-t('Кол-во передаваемых принтеров: ')), 'xerox': int(input('Кол-во передаваемых ксероксов: '))})
except ValueError:
    print('Вводите число')
    x.postuplenie({'scanner': int(input('Кол-во поступаемых сканеров: ')), 'printer': int(input('Кол-во поступаемых принтеров: ')), 'xerox': int(input('Кол-во поступаемых ксероксов: '))})
    x.spisanie({'scanner': int(input('Кол-во списываемых сканеров: ')), 'printer': int(input('Кол-во списываемых принтеров: ')), 'xerox': int(input('Кол-во списываемых ксероксов: '))})
