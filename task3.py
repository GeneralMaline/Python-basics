def maxsum(a, b, c):
    m = min (a, b, c)
    s = a + b + c - m
    return s
print(maxsum(float(input("Введите 1-е число ")), float(input("Введите 2-е число ")), float(input("Введите 3-е число "))))
