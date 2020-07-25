with open('text_6.txt', 'r', encoding='utf-8') as _file:
    stroki = _file.read().split('\n')#Разбивает файл на строки
    dict = dict()
    summ = 0
    for i in stroki:#переменная становится строкой
        stroka = i.split()#разбивает строку на отдельные элементы
        chislo = ''
        for n in stroka:# переменная принимает значение элементов строки
            for k in n.split('('):#переменная принимает значение символов элемента
                if k.isdigit():#поиск чисел
                    chislo = chislo + k
                try:
                    summ = summ + int(chislo)
                    chislo = ""#После подсчета суммы в строке обнуляет "число"
                except ValueError:
                    continue
        dict[stroka[0]] = summ
        summ = 0#После сохранения суммы в словаре обнуляет сумму
print(dict)

#Получился Франкенштейн какой-то