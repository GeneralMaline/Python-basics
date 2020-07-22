import functools
li = [i for i in range(100, 1001) if i % 2 == 0]
def fu(a, b):
    return a * b
print(functools.reduce(fu, li))