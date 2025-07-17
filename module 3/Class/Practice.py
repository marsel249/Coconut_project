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


# class Account:
#     def __init__(self, balance, name=None):
#         if balance < 0:
#             raise ValueError('Balance < 0')
#         self.balance = balance
#         self.name = name
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError('Dep <= 0')
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError('Withdraw <= 0')
#         if self.balance > amount:
#             self.balance -= amount
#             return self.balance
#         else:
#             # return (f'Вывод невозможен, '
#             #         f'balance:{self.balance} < withdraw amount: {amount}')
#             raise (f'Вывод невозможен, '
#                     f'balance:{self.balance} < withdraw amount: {amount}')
#
# class SavingsAccount(Account):
#     def __init__(self, balance, name=None, interest_rate=None):
#         super().__init__(balance, name)
#         self.interest_rate = interest_rate
#         if interest_rate <= 0:
#             raise f'% < 0'
#         # self.balance *= interest_rate
#
#     def withdraw(self, amount):
#         min_bal = 100
#         if amount <= 0:
#             raise ValueError('Withdraw <= 0')
#         if self.balance > amount + min_bal:
#             self.balance -= amount
#             return self.balance
#         else:
#             # return (f'Вывод невозможен, '
#             #         f'balance:{self.balance} + 100 < withdraw amount: {amount}')
#             raise (f'Вывод невозможен, balance:{self.balance} + 100 < withdraw amount: {amount}')
#
#     def invest(self):
#         drop = self.balance * self.interest_rate
#         self.balance += drop
#         return self.balance
#
#     def invest1(self, new_interest_rate):
#         drop = self.balance * new_interest_rate
#         self.balance += drop
#         return self.balance
#
#     def __str__(self): #При принте экземляра класса, print(x) например - делает принт с нужной информацией
#         return f'balance: {self.balance}, %: {self.interest_rate}'
#
#
# # x = Account(balance=110)
# # print(x.deposit(100))
# # print(x.withdraw(90))
# # print(x.balance)
#
# x = SavingsAccount(balance=110, interest_rate=0.1)
# print(round(x.balance))
# # print(round(x.withdraw(200)))
# print(x.withdraw(5))
# print(x.invest())
# x.interest_rate = 0.3
# print(x.invest())
# # print(x.invest1(999))
# # print(x.deposit(99999999999999))
# print(x)

'''Пример из видео курса'''

# class Character:
#     def __init__(self, level):
#         self.level = level
#         self.health_pooints = self.base_health_pooints * self.level
#         self.attack_power = self.base_attack_power * self.level
#
#     def attack(self):
#         print(f'{self.name_character} attack with {self.attack_power}')
#
#     def __str__(self):
#         return f'{self.name_character}, {self.level} lvl, attack: {self.attack_power}, hp: {self.health_pooints}'
#
# class Okr(Character):
#     name_character = 'Ork'
#     base_health_pooints = 100
#     base_attack_power = 10
#
# class Elf(Character):
#     name_character = 'Elf'
#     base_health_pooints = 50
#     base_attack_power = 15
#
#     def attack(self):
#         return print(f'This is a new method!!11 ..elf attack: {self.attack_power}')
#
# New_ork = Okr(3)
# print(New_ork)
# New_ork.attack()
#
# New_elf = Elf(5)
# print(New_elf)
# New_elf.attack()

'''- **Задание#1**
    
    Создайте класс `Book` (Книга) со следующими атрибутами:
    
    - `title` (название) — строка
    - `author` (автор) — строка
    - `pages` (количество страниц) — целое число
    
    Реализуйте геттеры и сеттеры для всех атрибутов, используя `@property`. 
    В сеттере для `pages` добавьте проверку: количество страниц не может быть отрицательным. 
    Если передано отрицательное значение, выведите сообщение об ошибке и не изменяйте значение атрибута.
    
    **Пример использования ниже, саму реализацию класса напишите сами!**'''

# class Book:
#     def __init__(self, title, author, pages):
#         self._title = title
#         self._author = author
#         self._pages = pages
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, new_title):
#         self._title = new_title
#
#     @property
#     def author(self):
#         return self._author
#
#     @author.setter
#     def author(self, new_author):
#         self._author = new_author
#
#     @property
#     def pages(self):
#         return self._pages
#
#     @pages.setter
#     def pages(self, new_pages):
#         if new_pages < 0:
#             # raise 'Pages < 0'
#             print("Количество страниц не может быть отрицательным.")
#         else:
#             self._pages = new_pages
#
# book = Book('Война и мир', 'Лев Толстой', 1300)
# # print(book.title)
# # book.pages = -2
# # print(book.pages)
#
# book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)
# print(book.title)  # Вывод: Мастер и Маргарита
# book.pages = -10  # Вывод: Количество страниц не может быть отрицательным.
# print(book.pages) #вывод 384
# book.pages = 400
# print(book.pages) #вывод 400

'''- Задание#2
    
    Создайте класс `BankAccount` (Банковский счет) со следующими атрибутами:
    
    - `account_number` (номер счета) — строка
    - `balance` (баланс) — число (можно использовать float)
    
    Реализуйте геттер для `balance` и сеттер, который позволяет только *увеличивать* 
    баланс (вносить деньги на счет). При попытке уменьшить баланс (снять деньги) выведите сообщение: 
    "Операция снятия средств не поддерживается. Используйте метод withdraw()". 
    Также реализуйте метод `withdraw(amount)` (снять `amount` денег), который уменьшает баланс. 
    Добавьте проверку, что `amount` не может быть отрицательным и не может превышать текущий баланс'''

# class BankAccount:
#     def __init__(self, account_number:str, balance:float):
#         self._account_number = account_number
#         self._balance = balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             print(f'Операция снятия средств не поддерживается. Используйте метод withdraw()')
#         else:
#             self._balance += amount
#             return self._balance
#
#     def withdraw(self, amount):
#         if self._balance < amount:
#             print('amount не может превышать текущий баланс')
#         elif amount < 0:
#             print('amount не может быть отрицательным')
#         else:
#             self._balance -= amount
#             return self._balance
#
# x = BankAccount(999, 1000)
# print(x.balance)
# x.withdraw(100)
# print(x.balance)
# x.balance = 500
# print(x.balance)
# x.withdraw(1401)
# print(x.balance)
