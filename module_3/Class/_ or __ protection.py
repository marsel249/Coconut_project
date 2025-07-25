'''_variable'''
# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance  # Защищенный атрибут
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Сумма депозита должна быть положительной.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance :
#             self._balance -= amount
#         else:
#             print("Недостаточно средств или некорректная сумма.")
#
#     def get_balance(self):
#         return self._balance
#
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(2000)
# print(account.get_balance())
# """Мы можем обратиться к защищенному атрибуту напрямую, но это не рекомендуется"""
# print(account._balance)  # Вывод: 1500 (но лучше использовать account.get_balance())
#
# account._balance = -1000 #можем изменить напрямую, но это плохо
# print(account.get_balance()) #вывод -1000, что недопустимо
# account.withdraw(100)
# print(account.get_balance()) #вывод -1000, что недопустимо

#_________

'''__variable'''
# Без искажения имен

# class Parent:
#     def __init__(self):
#         self.attribute = "Parent attribute"
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()  # Вызываем конструктор родительского класса
#         self.attribute = "Child attribute"
#
# parent = Parent()
# child = Child()
#
# print(parent.attribute)  # Вывод: Parent attribute
# print(child.attribute)   # Вывод: Child attribute

# С искажением имен

# class Parent:
#     def __init__(self):
#         self.__attribute = "Parent attribute"
#
#     def get_parent_attribute(self):  # Вот здесь еще метод для обращения к атрибуту
#         return self.__attribute
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__attribute = "Child attribute"
#
#     def get_child_attribute(self):  # И тут еще метод для обращения к атрибуту
#         return self.__attribute
#
# parent = Parent()
# child = Child()
#
# print(parent.get_parent_attribute())  # Вывод: Parent attribute
# print(child.get_parent_attribute()) # Вывод: Parent attribute (благодаря искажению имен)
# print(child.get_child_attribute())  # Вывод: Child attribute
#
# # Прямой доступ к "приватным" атрибутам (используя искаженное имя):
# print(parent._Parent__attribute) #вывод Parent attribute
# print(child._Parent__attribute) #вывод Parent attribute
# print(child._Child__attribute) #вывод Child attribute


