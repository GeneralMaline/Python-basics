def my_f(a, b):
    return a / b
try:
    a1 = float(input("Введите делимое "))
    b1 = float(input("Введите делитель "))
    if b1 == 0:
        print("Ошибка! Деление на 0.")
        a1 = float(input("Введите делимое "))
        b1 = float(input("Введите делитель "))
except ValueError:
    print("Ошибка! Введите ЧИСЛО")
    a1 = float(input("Введите делимое "))
    b1 = float(input("Введите делитель "))
print("a / b = ", my_f(a1, b1))

"""Try except с делением на 0 не получилось почему-то"""