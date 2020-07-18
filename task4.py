def func(x, y):
    i = 1
    res = 1 / x
    i = i + 1
    while 1 < i <= abs(y):
        res = res / x
        print(f"i = {i}, res = {res}")
        i = i + 1
    #x = x ** y
    return round(res, 4)
print(func(int(input ("Введите целое положительное число ")), int(input ("Введите целое отрицательное число "))))