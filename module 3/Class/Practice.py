'''Задание#1

1. Создать класс `Book` с атрибутами `title` (название), `author` (автор) и `pages` (количество страниц)
2. Сделать на его основе объект
3. Вывести при помощи `print()` атрибуты этого объекта
4. После изменить для конкретного объекта title и вывести его, дабы убедиться что он изменился.
5. Добавить новый атрибут объекту и тоже его вывести при помощи `print()`'''
from time import clock_settime

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     # def get_info(self):
#     #     return self.title, self.pages, self.author
#
# my_book = Book('Война и Мир','Лев Толстой',1300)
# # print(my_book.get_info())
# print(my_book.title)
# print(my_book.author)
# my_book.author = 'Lev Nikolayevich Tolstoy'
# print(my_book.author)
# my_book.state = 'old'
# print(my_book.state)

'''- Задание#1

    Создай класс `Animal` с атрибутами `name` и `age`, методом `speak()`, который выводит "I am an animal". Затем:

    1. Доработай метод `speak()`, чтобы он использовал атрибуты `name` и `age`, и использовал их в выводе. 
    Например: "I am an animal, my name is {name} and my age {age}"
    2. Создай объект класса `Animal` и вызови метод `speak()`
    3. Измени атрибуты созданного раннее объекта, присвоив новые `name` и `age`
    4. Снова вызови метод `speak()` и убедись, что в выводе `name` и `age` изменились'''

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print(f'my name: {self.name}, age: {self.age}, I am an animal')
#
# cat = Animal('Sherlock', 8)
# cat.speak()
# cat.name = 'Barsik'
# cat.age = 38
# cat.speak()
#
# # class Cat(Animal):
# #     def speak(self):
# #         print('Meow!!11')
# #
# # cat = Cat('Sherlock', 8)
# # cat.speak()

'''- Задание#2

    Давай оставим Human и Animal позади и сделаем что-нибудь полезное

    Создай класс, объект которого сможет принять 2 числа, а на выходе:

    1. Метод вернет то число, которое больше
    2. Выведет какое это число - четное или нечетное
    3. Скажет, положительное это число, отрицательное или ноль'''

# class ClassName:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def mymath1(self):
#         if self.a > self.b:
#             # print(f'{self.a} > {self.b}')
#             # return f'{self.a} > {self.b}'
#             return self.a
#         elif self.a == self.b:
#             return self.a
#         else:
#             # print(f'{self.a} < {self.b}')
#             # return f'{self.a} < {self.b}'
#             return self.b
#
#     def mymath2(self):
#         result_math1 = self.mymath1()
#         if result_math1 > 0:
#             print(f'{result_math1} > 0')
#         elif result_math1 < 0:
#             print(f'{result_math1} < 0')
#         else:
#             print(f'{result_math1} = 0')
#
#     def mymath3(self):
#         result_math1 = self.mymath1()
#         if result_math1 % 2 == 0:
#             print(f'{result_math1} - четное')
#         else:
#             print(f'{result_math1} - не четное')
#
#     def mymath4(self):
#         self.mymath2()
#         self.mymath3()
#
# my_example = ClassName(5, 10)
# # my_example.mymath2()
# # my_example.mymath3()
# my_example.mymath4()

'''Создать программу, моделирующую работу учетной системы
У нас есть базовый класс Account (счет), а также дочерний класс SavingsAccount (сберегательный счет), 
который добавляет дополнительное поле — процент на остаток средств:

### **Требования:**

1. Создать базовый класс `Account`, который:
    - Принимает `name` (имя владельца) и `balance` (баланс) при создании
    - Проверяет, что начальный баланс (`balance`) не может быть отрицательным. 
    Если отрицательный — выбрасывает исключение `ValueError`
    - Содержит метод `deposit(amount)`, который добавляет сумму на баланс
    - Содержит метод `withdraw(amount)`, который уменьшает баланс, но не допускает, чтобы баланс стал отрицательным
2. Создайте дочерний класс `SavingsAccount`, который:
    - Унаследует все атрибуты и методы `Account`
    - Имеет дополнительный атрибут `interest_rate` (процент на остаток) при создании
    - Расширяет метод `withdraw(amount)` так, чтобы при выводе средств оставался минимальный остаток (например, 100)'''


class Account:
    def __init__(self, balance, name=None):
        if balance < 0:
            raise ValueError('Balance < 0')
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Dep <= 0')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdraw <= 0')
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        else:
            # return (f'Вывод невозможен, '
            #         f'balance:{self.balance} < withdraw amount: {amount}')
            raise (f'Вывод невозможен, '
                    f'balance:{self.balance} < withdraw amount: {amount}')

class SavingsAccount(Account):
    def __init__(self, balance, name=None, interest_rate=None):
        super().__init__(balance, name)
        self.interest_rate = interest_rate
        if interest_rate <= 0:
            raise f'% < 0'
        # self.balance *= interest_rate

    def withdraw(self, amount):
        min_bal = 100
        if amount <= 0:
            raise ValueError('Withdraw <= 0')
        if self.balance > amount + min_bal:
            self.balance -= amount
            return self.balance
        else:
            # return (f'Вывод невозможен, '
            #         f'balance:{self.balance} + 100 < withdraw amount: {amount}')
            raise (f'Вывод невозможен, balance:{self.balance} + 100 < withdraw amount: {amount}')

    def invest(self):
        drop = self.balance * self.interest_rate
        self.balance += drop
        return self.balance

    def invest1(self, new_interest_rate):
        drop = self.balance * new_interest_rate
        self.balance += drop
        return self.balance



# x = Account(balance=110)
# print(x.deposit(100))
# print(x.withdraw(90))
# print(x.balance)

x = SavingsAccount(balance=110, interest_rate=0.1)
print(round(x.balance))
# print(round(x.withdraw(200)))
print(x.withdraw(5))
print(x.invest())
x.interest_rate = 0.3
print(x.invest())
print(x.invest1(999))
print(x.deposit(99999999999999))




