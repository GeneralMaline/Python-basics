class car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'The car {self.color} {self.name} has start moving')
    def stop(self):
        print(f'The car {self.color} {self.name} stopped\n')
    def turn(self):
        print(f'The car {self.color} {self.name} has turned left')
    def show_speed(self):
        print(f'The car {self.color} {self.name} is moving at speed of {self.speed}')
    def woop(self):
        if self.is_police == True:
            print('Woop! Woop! Thats the sound of the Police!')


class towncar(car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is too high. Please, speed down.')
        else:
            print(f'The car {self.color} {self.name} is moving at speed of {self.speed}')

class sportcar(car):
    pass

class workcar(car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Your speed is too high. Please, speed down.')
        else:
            print(f'The car {self.color} {self.name} is moving at speed of {self.speed}')

class policecar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = towncar(70, 'blue', 'Toyota Vitz', False)
a.woop()
a.go()
a.turn()
a.show_speed()
a.stop()

b = sportcar(120, 'red', 'Aston Martin DB7', False)
b.woop()
b.go()
b.turn()
b.show_speed()
b.stop()

c = workcar(40, 'white', 'Nissan Atlas', False)
c.woop()
c.go()
c.turn()
c.show_speed()
c.stop()

d = policecar(90, 'black', 'Ford Interceptor', True)
d.woop()
d.go()
d.turn()
d.show_speed()
d.stop()