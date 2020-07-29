class stationery():
    def __init__(self):
        self.title = input('Введите название: ')
    def draw(self):
        print('запуск отрисовки')
class pen(stationery):
    def draw(self):
        print('ручка')
class pencil(stationery):
    def draw(self):
        print('карандаш')

class handle(stationery):
    def draw(self):
        print('маркер')


a = pen()
a.draw()

b = pencil()
b.draw()

c = handle()
c.draw()