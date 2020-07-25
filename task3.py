with open('text_3.txt', 'r', encoding='utf-8') as _file:
    employees = ""
    zp = 0
    stroki = _file.read().split("\n")
    for i in range(len(stroki)):
        stroka = stroki[i].split()
        zp = zp + float(stroka[1])
        if float(stroka[1]) < 20000:
            employees = employees + stroka[0] + ' '
    print('Сотрудники, чья ЗП меньше 20000: ', employees.split())
    print("средняя зарплата: ", zp / len(stroki))
