import json
with open('text_7.txt', 'r', encoding='utf-8') as _file:
    kolvo = 0
    summ = 0
    dict1 = dict()
    stroka = _file.read().split('\n')
    for i in stroka:
        pribyl = int(i.split()[2]) - int(i.split()[3])
        if pribyl >= 0:
            summ = summ + pribyl
            kolvo = kolvo + 1
        dict1[i.split()[0]] = pribyl
    avr = summ / kolvo
    dict2 = {'average': avr}
with open('text7json.json', 'w', encoding='utf-8') as jfile:
    json.dump([dict1, dict2], jfile)
    #Не смог разобраться в форматировании json