'''Задание#1

**Реестр животных**
Создай класс `Animal` с атрибутом класса `species` (список всех зарегистрированных видов животных)
Реализуй метод класса `add_species`, который добавляет новый вид в реестр при создании объекта,
 и метод `show_species`, который выводит список всех видов
При этом, если уже в реестре есть такой тип животного, то `add_species` не должен его добавлять в этот реестр.'''
from tkinter.font import names

# class Animal:
#
#     species = []
#
#     def __init__(self, name):
#         self.name = name
#         Animal.species.append()

# class Animal:
#     species = []
#
#     def __init__(self, name):
#         self.name = name
#         # self.__class__.species.append(name)
#         # Animal.species.append()
#         # Animal.species.append(name)
#
#     @classmethod
#     def add_species(cls, name):
#         cls.species.append(name)
#         # cls.species.append(cls.__name__)
#         return cls.species
#
# cat1 = Animal('cat1')
# cat2 = Animal('cat2')
# cat3 = Animal('cat3')
# print(Animal.add_species('cat999'))



# class Animal:
#     species = []
#
#     def __init__(self, name):
#         self.name = name
#         # self.__class__.species.append(name)
#         # Animal.species.append()
#         # Animal.species.append(name)
#
#     @classmethod
#     def add_species(cls, name):
#         if name not in cls.species:
#             cls.species.append(name)
#         # cls.species.append(name) #Добавляет имя в список животных
#         # cls.species.append(cls.__name__)
#
#     @classmethod
#     def show_species(cls):
#         return cls.species
#
# cat1 = Animal('cat1')
# cat2 = Animal('cat2')
# cat3 = Animal('cat3')
# Animal.add_species('cat888')
# Animal.add_species('cat111')
# Animal.add_species('cat111')
# # print(Animal.add_species('cat999'))
# print(Animal.show_species())


'''Вариант нейросети'''

# class Animal:
#     species = []  # Реестр всех видов животных (атрибут класса)
#
#     def __init__(self, name):
#         """
#         Создает животное и регистрирует его вид
#         :param name: название вида животного
#         """
#         self.name = name
#         self.__class__.add_species(name)  # Автоматическая регистрация при создании
#
#     @classmethod
#     def add_species(cls, name):
#         """
#         Добавляет вид животного в реестр, если его там еще нет
#         :param name: название вида для добавления
#         """
#         if name not in cls.species:  # Проверяем, нет ли уже такого вида
#             cls.species.append(name)
#             print(f'Вид "{name}" добавлен в реестр')
#         else:
#             print(f'Вид "{name}" уже есть в реестре')
#
#     @classmethod
#     def show_species(cls):
#         """
#         Возвращает список всех зарегистрированных видов
#         """
#         return cls.species
#
#
# # Демонстрация работы
# Animal.add_species('Слон')  # Вид "Слон" добавлен в реестр
# Animal.add_species('Тигр')  # Вид "Тигр" добавлен в реестр
# Animal.add_species('Слон')  # Вид "Слон" уже есть в реестре
#
# cat = Animal('Кошка')  # Вид "Кошка" добавлен в реестр (автоматически)
# dog = Animal('Собака')  # Вид "Собака" добавлен в реестр (автоматически)
#
# print("Все виды животных:", Animal.show_species())

'''Создание объектов через cls()'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def create_anonymous(cls): #метод класса
#       return cls("Anonymous", 0)
#
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")
#
# # Обычное создание объекта
# person1 = Person("Alice", 30)
# person1.introduce()
#
# # Создание объекта через метод класса
# person2 = Person.create_anonymous()
# person2.introduce()
# print(type(person1))
# print(type(person2))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'My name: {self.name}, age: {self.age}'
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         current_year = 2024
#         age = current_year - birth_year
#         return cls(name, age)  # Создаем объект Person!
#
# person1 = Person("Ivan", 30)                 #обычный способ создания объекта
# person2 = Person.from_birth_year("Petr", 1995)  # Используем метод класса
#
# print(person1)
# print(person2)
# print(person1.name, person1.age)
# print(person2.name, person2.age)

'''Статические методы (@staticmethod)'''


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#     @staticmethod
#     def is_positive(x):
#         return x > 0
#
#
# # Использование статических методов
# print(MathUtils.add(5, 7))  # Вывод: 12
# print(MathUtils.multiply(3, 4))  # Вывод: 12

# math = MathUtils()
# math.multiply(2, 3)  # Вывод: 6

'''Задание№1

Конвертер валют Создайте класс CurrencyConverter с методами:

usd_to_eur(amount): Конвертирует сумму в USD в EUR по курсу 0.85
eur_to_usd(amount): Конвертирует сумму в EUR в USD по курсу 1.18'''

# class CurrencyConverter:
#     @staticmethod
#     def usd_to_eur(amount):
#         usd_to_eur_price = 0.85
#         return amount * usd_to_eur_price
#
#     def eur_to_usd(amount):
#         eur_to_usd_price = 1.18
#         return amount * eur_to_usd_price
#
# print(CurrencyConverter.usd_to_eur(10))
# print(CurrencyConverter.eur_to_usd(10))



