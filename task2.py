_list = list()
i = 1
n = int(input("Введите количество элементов списка: "))
while i <= n:
    _list.append(input("Введите элемент списка: "))
    i = i + 1
#a = _list[::2]
#print(_list)
#print(a)
b = 0
while b < n:
    _list.insert(b + 2, _list[b])
    _list.pop(b)
    b = b + 2
print(_list)