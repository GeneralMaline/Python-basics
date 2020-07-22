from math import factorial
def fact(n):
    for el in (range(1, n + 1)):
        yield factorial(el)
i = 1
for el in fact(int(input("Введите число: "))):
    print(f"Факториал {i}! = {el}")
    i += 1