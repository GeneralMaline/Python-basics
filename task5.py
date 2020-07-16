my_list = [7, 5, 3, 3, 2]
print(my_list)
#print(my_list[::-1])
n = int(input("Введите число: "))
a = len(my_list)-1
for i in my_list[::-1]:
    a = a - 1
    if n <= i:
        my_list.insert(a + 2, n)
        break
    if n > my_list[0]:
        my_list.insert(0, n)
        break
print(my_list)

#Почему у одинаковых элементов в списке одинаковый индекс?