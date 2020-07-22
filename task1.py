#from sys import argv
#name, hours, stavka, prem = argv

import sys
name, hours, stavka, prem = sys.argv

print("Название скрипта: ", name)
print("Выработка в часах: ", hours)
print("Ставка в час: ", stavka)
print("Премия: ", prem)
print("Зарплата сотрудника: ", int(hours) * float(stavka) + float(prem))