with open('text1.txt', 'w', encoding='utf-8') as _file:
    while True:
        content = input('Введите строку(пустая строка - конец программы): ')
        if content != "":
            print(content, end = '\n', file = _file)
        else:
            break