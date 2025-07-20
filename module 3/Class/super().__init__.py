# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print(f"Родитель: {self.name}")
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Вызов Parent.__init__()
#         self.age = age
#         print(f"Ребенок: {self.name}, {self.age} лет")
#
# child = Child("Анна", 5)

# Вывод
# Родитель: Анна
# Ребенок: Анна, 5 лет


# class Animal:
#     def make_sound(self):
#         print("Какой-то звук")
#
# class Cat(Animal):
#     def make_sound(self):
#         super().make_sound()  # Сначала вызов родительского метода
#         print("Мяу!")
#
# cat = Cat()
# cat.make_sound()

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