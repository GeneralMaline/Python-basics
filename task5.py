_list = input("Введите числа через пробел ").split()
i = 0
res = 0
while _list[i] != "q":
    res = res + int(_list[i])
    if i == len(_list) - 1:
        print(res)
        _list.extend(input("Введите числа через пробел ").split())
    i += 1
print(res)

"""Похоже, я немного не так решил, потому что решение к теме урока не относится"""