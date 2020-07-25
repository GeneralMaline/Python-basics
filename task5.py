import random
sum = 0
with open('text5.txt', 'w', encoding='utf-8') as _file:
    li = [str(random.randint(0, 20)) for i in range(int(input("Введите количество чисел: ")))]
    _file.write(' '.join(li))
    print(' '.join(li))
with open('text5.txt', 'r', encoding='utf-8') as _file:
    _list = _file.read().split()
    for i in _list:
        i = int(i)
        sum += i
print(sum)