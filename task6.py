def func(a):
    f = 0
    for i in range(len(a)):
        for f in range(len(a[i][f])):
            if 97 <= ord(a[i][f]) <= 122:
                a[i] = a[i].capitalize()
            else:
                a = "Все буквы должны быть буквами латинского алфавита в нижнем регистре"
    return a

print(' '.join(func(input("Введите слова через пробел ").split())))