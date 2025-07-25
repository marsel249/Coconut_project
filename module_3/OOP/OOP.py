#
# class House:
#     def __init__(self, floors, roof, material):
#         self.floors = floors  # Количество этажей
#         self.roof = roof      # Тип крыши
#         self.material = material  # Материал стен
#
# # Создаем два объекта дома
# house1 = House(2, "черепичная", "кирпич")
# house2 = House(1, "металлическая", "дерево")
#
# print("Дом 1:", house1.floors, "этажа,", "крыша:", house1.roof, "материал:", house1.material)
# print("Дом 2:", house2.floors, "этаж,", "крыша:", house2.roof, "материал:", house2.material)


'''Инкапсуляция'''

# Пример №1
# class Safe:
#     def __init__(self, code, balance):
#         self.__code = code  # Приватный код
#         self.__balance = balance  # Приватный баланс
#
#     def check_balance(self, code):
#         if code == self.__code:
#             return f"Баланс в сейфе: {self.__balance} золотых"
#         else:
#             return "Неверный код. Доступ запрещён."
#
# # Создаём сейф
# safe = Safe("1234", 1000)
#
# # Попробуем проверить баланс
# print(safe.check_balance("1234"))  # Баланс в сейфе: 1000 золотых
# print(safe.check_balance("0000"))  # Неверный код. Доступ запрещён.

# Пример №2

# class Product:
#     def __init__(self, name, price):
#         self.name = name  # Открытый атрибут
#         self.__price = price  # Приватный атрибут
#
#     # Геттер для получения значения атрибута price
#     @property
#     def price(self):
#         return self.__price
#
#     # Сеттер для изменения значения атрибута price
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Цена не может быть отрицательной!")
#         self.__price = value
#
# # Использование
# product = Product("Ноутбук", 50000)
#
# # Доступ к открытому атрибуту
# print(product.name)  # Ноутбук
#
# # Попытка получить доступ к приватному атрибуту (будет ошибка)
# # print(product.__price)
#
# # Работа с приватным атрибутом через геттер и сеттер
# print(product.price)  # 50000
# product.price = 45000  # Изменение цены
# print(product.price)  # 45000
#
# # Попытка установить некорректную цену
# # product.price = -100  # ValueError: Цена не может быть отрицательной!

# Пример №3


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner  # Открытый атрибут
#         self.__balance = balance  # Приватный атрибут
#
#     # Геттер для получения баланса
#     @property
#     def balance(self):
#         return self.__balance
#
#     # Метод пополнения для депозита
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} добавлено. Новый баланс: {self.__balance}")
#         else:
#             print("Сумма должна быть положительной!")
#
#     # Метод для снятия денег
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} снято. Новый баланс: {self.__balance}")
#         else:
#             print("Недостаточно средств или некорректная сумма.")
#
# # Использование
# account = BankAccount("Иван", 1000)
# print(account.balance)  # 1000
# account.deposit(500)  # 500 добавлено. Новый баланс: 1500
# account.withdraw(200)  # 200 снято. Новый баланс: 1300

'''Наследование'''

# Пример №1

# Базовый класс
# class Hero:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(f"{self.name} бежит")
#
#     def fight(self):
#         print(f"{self.name} борется с врагом")
#
# # Дочерний класс
# class SpiderMan(Hero):  # Наследуем класс Hero
#     def shoot_web(self):
#         print(f"{self.name} выпускает паутину")
#
# # Создаём героя
# hero = SpiderMan("Человек-Паук")
# hero.run()  # Человек-Паук бежит
# hero.fight()  # Человек-Паук борется с врагом
# hero.shoot_web()  # Человек-Паук выпускает паутину

# Пример №2

# Родительский класс
# class Animal:
#     def breathe(self):
#         print("Дышит")
#
#     def eat(self):
#         print("Ест")
#
# # Дочерний класс
# class Bird(Animal):  # Наследуем класс Animal
#     def fly(self):
#         print("Летит")
#
# # Создаём птицу
# sparrow = Bird()
# sparrow.breathe()  # Дышит
# sparrow.eat()  # Ест
# sparrow.fly()  # Летит

# Пример №3


# Родительский класс
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} издаёт звук."
#
# # Дочерний класс Dog
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} лает."
#
# # Дочерний класс Cat
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} мяукает."
#
#
# # Создаем объекты
# dog = Dog("Барбос")
# cat = Cat("Мурзик")
#
# # Вызываем методы
# print(dog.speak())  # Барбос лает.
# print(cat.speak())  # Мурзик мяукает.

'''Полиморфизм'''

# Пример №1

# class Instrument:
#     def play(self):
#         raise NotImplementedError("Метод должен быть переопределён в дочернем классе")
#
# class Piano(Instrument):
#     def play(self):
#         print("Пианино играет мелодию")
#
# class Guitar(Instrument):
#     def play(self):
#         print("Гитара играет аккорды")
#
# class Drums(Instrument):
#     def play(self):
#         print("Барабаны задают ритм")
#
# # Оркестр
# instruments = [Piano(), Guitar(), Drums()]
#
# for instrument in instruments:
#     instrument.play()
#
# print(type(instruments))
# print(type(Piano()))

# Пример №2


# class Delivery:
#     def deliver(self):
#         raise NotImplementedError("Метод должен быть переопределён в дочернем классе")
#
# class Car(Delivery):
#     def deliver(self):
#         print("Доставляет на машине")
#
# class Bike(Delivery):
#     def deliver(self):
#         print("Доставляет на велосипеде")
#
# class Drone(Delivery):
#     def deliver(self):
#         print("Доставляет на дроне")
#
# # Система доставки
# vehicles = [Car(), Bike(), Drone()]
#
# for vehicle in vehicles:
#     vehicle.deliver()

# Пример №3


# # Родительский класс
# class Animal:
#     def speak(self):
#         return "Животное издаёт звук."
#
# # Дочерний класс Dog
# class Dog(Animal):
#     def speak(self):
#         return "Собака лает."
#
# # Дочерний класс Cat
# class Cat(Animal):
#     def speak(self):
#         return "Кошка мяукает."
#
# #Применение
#
# # Общая функция для работы с животными
# def make_sound(animal):
#     print(animal.speak())
#
# # Создаем объекты
# dog = Dog()
# cat = Cat()
#
# # Используем один метод для разных объектов
# make_sound(dog)  # Собака лает.
# make_sound(cat)  # Кошка мяукает.
#
# print(dog.speak())
# print(cat.speak())

'''Абстракция'''

# Пример №1

#Инкапсуляция, пример:

# class Safe:
#     def __init__(self, code):
#         self.__code = code  # Приватный атрибут
#
#     def open_safe(self, input_code):
#         if input_code == self.__code:
#             print("Сейф открыт!")
#         else:
#             print("Неверный код!")

#Абстракция, пример:

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     def start_engine(self):
#         print("Двигатель машины запущен")
#
# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Двигатель мотоцикла запущен")
#
# # Использование
# vehicles = [Car(), Motorcycle()]
# for vehicle in vehicles:
#     vehicle.start_engine()



#Пример абстракции

# from abc import ABC, abstractmethod #что такое импорт?
#
# # Абстрактный класс
#
# '''Тут мы написали абстрактный класс'''
# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# '''Здесь мы реализовали работу с абстрактным классом'''
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def draw(self):
#         return "Рисуем круг"
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def draw(self):
#         return "Рисуем прямоугольник"
#
#     def area(self):
#         return self.width * self.height
#
# '''Использование методов'''
#
# shapes = [Circle(5), Rectangle(4, 6)]
#
# for shape in shapes:
#     print(shape.draw())
#     print("Площадь:", shape.area())
#
# print(Circle(5).draw())
# print("Площадь:", Circle(5).area())

#Пример 2

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Собака лает."
#
# class Cat(Animal):
#     def speak(self):
#         return "Кошка мяукает."

#____

'''Пример реализации ООП'''


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#
#     def borrow(self):
#         self.is_borrowed = True
#
#     def return_book(self):
#         self.is_borrowed = False
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
#
#     def borrow_book(self, book):
#         if not book.is_borrowed:
#             book.borrow()
#             self.borrowed_books.append(book.title)
#         else:
#             print(f"Книга '{book.title}' уже занята.")
#
#     def return_book(self, book):
#         if book.title in self.borrowed_books:
#             book.return_book()
#             self.borrowed_books.remove(book.title)
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def list_books(self):
#         for book in self.books:
#             status = "Занята" if book.is_borrowed else "Свободна"
#             print(f"{book.title} ({book.author}) - {status}")












