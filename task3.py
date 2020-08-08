class MyError (Exception):
    def __init__ (self, txt):
        self.txt = txt

_list = []

while True:
        content = input('Введите число, для остановки введите q: ')
        if content != "q":
            try:
                if content.isdigit() == True:
                    _list.append(content)
                else:
                    raise MyError(f'Введите число, "{content}" не является числом')
            except (MyError) as e:
                print(e)
        else:
            break
print(_list)
