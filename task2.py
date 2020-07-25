with open("text1.txt", "r", encoding="utf-8") as _file:
    stroka = _file.read()
    print('Содержимое файла:\n', stroka)
    print('Количество строк: ', stroka.count('\n'))
    _file.seek(0)
    for i in range(1, stroka.count('\n') + 1):
        print(f'Количество слов в строке {i}: ', len(_file.readline().split()))
