# class NewObject:
#     pass
#
# object1 = NewObject()
# object2 = NewObject()

# class NewObject:
#     def __innit__(self):
#         print('Ты создал объект "Object"')
#
# object1 = NewObject()
# object2 = NewObject()
#____________

# class NewCar():
#     '''Описываем свойства объекта, методы объекта'''
#     def __init__(self, brand, color, drive, parking):
#         self.brand = brand
#         self.color = color
#         self.drive = drive
#         self.parking = parking
#
#     def status(self, drive, parking):
#         print(f'{self.drive}, {self.parking}')
#
# car1 = NewCar('BMW', 'Black', 'in drive', 'not stop')
# print(car1.status)

#____________
# class Fruit:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class Apple(Fruit):
#     def taste(self):
#         print(f'{self.name} сладкое.')
#
#
# class Banana(Fruit):
#     def taste(self):
#         print(f'{self.name} мягкий.')
#
#
# fruit = Fruit(name="Фрукт")
# print(fruit.get_name())
#
# apple = Apple(name="Яблоко")
# print(apple.get_name())
# apple.taste()
#
# banana = Banana(name="Банан")
# print(banana.get_name())
# banana.taste()
#____________

'''Пример работы'''
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"Марка: {self.make}, Модель: {self.model}, Год: {self.year}"
#
#
# class Car(Vehicle):
#     def start_engine(self):
#         print(f"Машина {self.model} завелась!")
#
#
# class Bicycle(Vehicle):
#
#     def ring_bell(self):
#         print(f"Звенит звонок велосипеда {self.model}!")
#
#
# vehicle = Vehicle("Москвич", "412", "1977")
# cybertruck = Car("Tesla", "Cybertruck", "2023")
# orlenok = Bicycle("Вайрас", "Орлёнок", "1962")
# print(vehicle.get_info())
# print(cybertruck.get_info())
# cybertruck.start_engine()
# print(orlenok.get_info())
# orlenok.ring_bell()


#________________

# class Employee:
#     company_name = "TechCorp"  # Атрибут класса
#
#     def __init__(self, name, position):
#         self.name = name  # Атрибут объекта
#         self.position = position  # Атрибут объекта
#
#     def display_info(self):
#         print(f"{self.name} works as a {self.position} at {Employee.company_name}.")
#
#
# # Создание объектов класса Employee
# emp1 = Employee("Alice", "Developer")
# emp2 = Employee("Bob", "Designer")
#
# emp1.display_info()  # Вывод: Alice works as a Developer at TechCorp.
# emp2.display_info()  # Вывод: Bob works as a Designer at TechCorp.
#
# # Изменение атрибута класса
# Employee.company_name = "DevSolutions"
# emp1.display_info()  # Вывод: Alice works as a Developer at DevSolutions.

#________________

# class ClassName:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def mymath(self):
#         if self.a > self.b:
#             return self.a
#         elif self.a == self.b:
#             return self.a
#         else:
#             return self.b
#
# class Comparison(ClassName):
#     def mymath1(self):
#         max_number = super().mymath()
#         if max_number > 0:
#             print(f'{max_number} > 0')
#         elif self.mymath() < 0:
#             print(f'{max_number} < 0')
#         else:
#             print(f'{max_number} = 0')
#
# class EvenNumber(ClassName):
#     def mymath2(self):
#         max_number = super().mymath()
#         if max_number % 2 == 0:
#             print(f'{max_number} - четное')
#         else:
#             print(f'{max_number} - не четное')
#
# x = EvenNumber(10,15)
# x.mymath2()
#
# x = Comparison(10,15)
# x.mymath1()

#_________
# class Animal:
#     def __init__(self, name):
#         print("Animal init called")
#         self.name = name
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         print("Dog init called")
#         super().__init__(name)  # Вызов __init__ родителя
#         self.breed = breed
#
# dog = Dog("Rex", "Bulldog")
# print(dog.name)  # Rex
# print(dog.breed)  # Bulldog
#_________

