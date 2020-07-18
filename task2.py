def func(name, lastname, year, city, email, phone):
    return (f"{name} {lastname} {year} {city} {email} {phone}")
print(func(name = input("Введите имя "), lastname = input("Введите фамилию "), year = input("Введите год рождения "), city = input("Введите город проживания "),  email = input("Введите почту "), phone = input("Введите номер телефона ")))