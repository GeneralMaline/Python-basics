n = int(input("Vvedite kolichestvo tovarov: "))
i = 1
my_list = list()
# my_list = list(tuple(a, {'название': _name, "цена": _price, "количество": _qty, "ед": _ed}))
while i <= n:
    my_list.append((i, {"название": input("Введите название товара: "), "цена": input("Введите стоимость товара: "),
                        "количество": input("Введите количество товара: "),
                        "единицы измерения": input("Введите единицы измерения: ")}))
    i = i + 1
print(my_list)
analytics = {"название": [], "цена": [], "количество": [], "единицы измерения": []}
for a in range(len(my_list)):
    analytics['название'].append(my_list[a][1]['название'])
    analytics['цена'].append(my_list[a][1]['цена'])
    analytics['количество'].append(my_list[a][1]['количество'])
    analytics['единицы измерения'].append(my_list[a][1]['единицы измерения'])
print(analytics)