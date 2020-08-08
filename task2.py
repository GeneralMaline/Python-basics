class MyError (Exception):
    def __init__ (self, txt):
        self.txt = txt

try:
    a = int(input("Введите число, которое будем делить "))
    b = int(input("Введите число, на которое будем делить "))
    if b == 0:
        raise MyError('На 0 делить нельзя!')
    a / b
except (ValueError, MyError) as err:
    print(err)
else:
    print(a / b)