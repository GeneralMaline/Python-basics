_list = input("Vvedite slova").split()
for i, n in enumerate(_list, 1):
    if len(n) > 10:
        n = n[:10]
    print(i, n)