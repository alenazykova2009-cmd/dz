#Задание 1
#class Person:
#    def __init__(self, fio, date, phone, city, country, address):
#        self._fio = fio
#        self._date = date
#        self._phone = phone
#        self._city = city
#        self._country = country
#        self._address = address

#    def input_data(self):
#        self._fio = input("Введите ФИО: ")
#        self._date = input("Введите дату рождения: ")
#        self._phone = input("Введите телефон: ")
#        self._city = input("Введите город: ")
#        self._country = input("Введите страну: ")
#        self._address = input("Введите адрес: ")
#
#    def get_fio(self):
#        return self._fio
#    def get_date(self):
#        return self._date
#    def get_phone(self):
#        return self._phone
#    def get_city(self):
#        return self._city
#    def get_country(self):
#        return self._country
#    def get_address(self):
#        return self._address
#
#    def display_data(self):
#        print("Данные человека:")
#        print("ФИО:", self.get_fio())
#        print("Дата рождения:", self.get_date())
#        print("Телефон:", self.get_phone())
#        print("Город:", self.get_city())
#        print("Страна:", self.get_country())
#        print("Адрес:", self.get_address())
#
#person = Person("","","","","", "")
#person.input_data()
#person.display_data()

# Задание 2

#class City:
#    def __init__(self, city, region, residents, index, code):
#        self._city = city
#        self._region = region
#        self._residents = residents
#        self._index = index
#        self._code = code

#    def input_city(self):
#        self._city = input("Введите город: ")
#        self._region = input("Введите регион: ")
#        self._residents = input("Введите количество жителей в городе: ")
#        self._index = input("Введите почтовый индекс города: ")
#        self._code = input("Введите телефонный код города: ")

#    def get_city(self):
#        return self._city
#    def get_region(self):
#        return self._region
#    def get_residents(self):
#        return self._residents
#    def get_index(self):
#        return self._index
#    def get_code(self):
#        return self._code

#    def display_data(self):
#        print("О городе:")
#        print("Название города:", self._city)
#        print("Регион:", self._region)
#        print("Кол-во жителей:", self._residents)
#        print("Почтовый индекс:", self._index)
#        print("Телефонный код:", self._code)

#city = City("","","","", "")
#city.input_city()
#city.display_data()

# Задание 3
#class Country:
#    def __init__(self, country_name, continent, residents, code, capital, cities_country):
#        self._country_name = country_name
#        self._continent = continent
#        self._residents = residents
#        self._code = code
#        self._capital = capital
#        self._cities_country = cities_country
#    def input(self):
#        self._country_name = input("Введите название страны: ")
#        self._continent = input("Введите название континента: ")
#        self._residents = input("Введите кол-во жителей: ")
#        self._code = input("Введите телефонный код страны: ")
#        self._capital = input("Введите название столицы: ")
#        self._cities_country = input("Введите название городов страны: ")

#    def country_name(self):
#        return self._country_name
#    def continent(self):
#        return self._continent
#    def residents(self):
#        return self._residents
#    def code(self):
#        return self._code
#    def capital(self):
#        return self._capital
#    def cities_country(self):
#        return self._cities_country
#
#    def display_data(self):
#        print("О стране:")
#        print("Название страны:", self._country_name)
#        print("Название континента:", self._continent)
#        print("Название страны:", self._residents)
#        print("Название страны:", self._code)
#        print("Название страны:", self._capital)
#        print("Название страны:", self._cities_country)
#
#ountry = Country("","","","","","")
#country.input()
#country.display_data()

#Задание 4

class Fraction:
    def __init__(self, nomerator, denominator):
        self._numerator = nomerator
        self._denominator = denominator

    def input(self):
        self._numerator = int(input("Введите числитель: "))
        self._denominator = int(input("Введите знаменатель: "))

    def numerator(self):
        return self._numerator
    def denominator(self):
        return self._denominator

    def display_data(self):
        print("Сложение:", self._numerator + self._denominator)
        print("Вычитание:", self._numerator - self._denominator)
        print("Деление:", self._numerator / self._denominator)
        print("Умножение:", self._numerator * self._denominator)

fraction = Fraction("", "")
fraction.input()
fraction.display_data()


