class data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converter(cls, datalist):
        try:
            day, month, year = datalist
            try:
                day = int(day)
                month = int(month)
                year = int(year)
                return cls(day, month, year)
            except ValueError:
                print('Введите дату ЧИСЛАМИ')
        except ValueError:
            print('Неверный формат даты')

    @staticmethod
    def valid(self):
        try:
            return f'Вы ввели дату: {self.day}-{self.month}-{self.year}' if 1 <= self.day <= 31 and 1 <= self.month <= 12 else "Некорректная дата"
        except AttributeError:
            return "Ошибка"

    # def __str__(self):

_date = input('Введите дату в формате ДД-ММ-ГГГГ: ').split('-')
a = data.converter(_date)
print(data.valid(a))