# class Person:
#     def __init__(self, name, age):
#         self._name = name  # _ показывает, что атрибут "внутренний"
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, new_name):
#         self._name = new_name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, new_age):
#         if new_age < 0:  # Проверка значения (возраст не может быть отрицательным)
#             print("Возраст должен быть неотрицательным!")
#         else:
#             self._age = new_age
#
# """Создаем объект класса Person"""
# person = Person("Иван", 25)
#
# """Используем сеттеры для установки значений (с частичной проверкой)"""
# person.set_age(-10)  # Вывод: Возраст должен быть неотрицательным!
#
# """Используем геттер для получения значения"""
# print(person.get_name())  # Вывод: Иван
#
# person.set_name("Алексей")
# print(person.get_name()) #вывод Алексей
# person.set_age(30)
# print(person.get_age()) #вывод 30