'''Задание 1: Зелье восстановления Тема: Функции.'''

'''1. Напишите функцию `restore_health`, которая принимает два параметра:
    - `current_health` — текущее здоровье героя.
    - `potion` — количество здоровья, восстанавливаемое зельем.
2. Если восстановленное здоровье превышает максимум (`max_health = 100`), установите здоровье равным `100`.
3. Верните новое значение здоровья.'''

# def restore_health(current_health, potion):
#     max_health = 100
#     health_after = current_health + potion
#     if health_after > max_health:
#         health_after = 100
#     return health_after
#
# print(restore_health(50, 30))
# print(restore_health(50, 60))

'''Задание 2: Гоблинский торговец Тема: Методы класса'''

'''1. Создайте класс `GoblinTrader`, который:
    - Имеет атрибут `gold` (количество золота у игрока).
    - Метод `buy_item`, который принимает `item_name` и `item_price`.
        - Если у игрока достаточно золота, уменьшает золото на цену предмета 
        и выводит сообщение об успешной покупке.
        - Если золота не хватает, выводит сообщение: "Недостаточно золота!"
2. Создайте объект `GoblinTrader` и протестируйте метод.'''

#Решение через захардкоженый голд, в классе, неправильно понял, какой метод должен быть использован в решении задачи

# class GoblinTrader:
#     gold = 100
#
#     @classmethod
#     def buy_item(cls, item_name, item_price):
#         if cls.gold > item_price:
#             cls.gold -= item_price
#             print(f'Куплен {item_name} за {item_price} золота, осталось золота: {cls.gold}')
#         else:
#             print(f'{item_name} стоимостью: {item_price}, не куплен, осталось: {cls.gold} золота')
#
# x = GoblinTrader()
# x.buy_item('Нож', 43)
# x.buy_item('Топор', 60)

#Переписал правильно
# class GoblinTrader:
#     def __init__(self, gold):
#         self.gold = gold
#
#     def buy_item(self, item_name, item_price):
#         if self.gold >= item_price:
#             self.gold -= item_price
#             print(f'Покупка {item_name}, за {item_price} золотых, остаток золота: {self.gold}')
#         else:
#             print(f'Неудачная покупка {item_name}, за {item_price}, остаток золота: {self.gold}')
#
# x = GoblinTrader(100)
# x.buy_item('Нож', 43)
# x.buy_item('Топор', 60)

'''Задание 2.1: Гоблинский торговец (Методы класса и статические методы)'''

'''**Тема:** Методы класса, статические методы, операции с золотом

1. Создайте класс `GoblinMerchant` с атрибутом экземпляра `gold`.
2. Добавьте статический метод `tax_rate()`, возвращающий 0.1 (10% налог).
3. Добавьте метод класса `from_rich_merchant(cls)`, создающий торговца с 1000 золота.
4. Реализуйте метод `buy_item(item_name, item_price)`:
    - Проверяет, достаточно ли золота.
    - Если достаточно: уменьшает золото на `item_price + item_price * tax_rate()`.
    - Возвращает сообщение о покупке.
    - Если золота не хватает, возвращает "Недостаточно золота!".
5. Протестируйте класс:
    - Создайте обычного торговца с 200 золота и попробуйте купить предмет за 150.
    - Создайте торговца через `from_rich_merchant()` и купите предмет за 500.'''

# class GoblinMerchant:
#     rich_man = 1000 #атрибут класса
#
#     def __init__(self, gold):
#         self.gold = gold #атрибут экземпляра
#
#     @staticmethod
#     def tax_rate(a):
#         if a > 0:
#             return a * 0.1
#
#     @classmethod
#     def from_rich_merchant(cls):
#         return cls(cls.rich_man) # gold = rich_man. cls() вместо GoblinMerchant()
#
#     def get_your_gold(self):
#         return self.gold
#
#     def buy_item(self, item_name, item_price):
#         item_with_tax = item_price + self.tax_rate(item_price)
#         if self.gold >= item_with_tax:
#             self.gold -= item_with_tax
#             return f'Был куплен {item_name}, за {item_price} + tax {round(item_with_tax - item_price, 2)}={item_with_tax}, осталось: {self.gold} золота'
#         else:
#             return f'Неудачная покупка {item_name}, за {item_price} + tax {round(item_with_tax - item_price, 2)}={item_with_tax}, остаталось: {self.gold} золота '
#
# x = GoblinMerchant(200)  # торговец с 200 золота
# y = GoblinMerchant.from_rich_merchant()  # торговец с 1000 золота
#
# print(x.get_your_gold())
# print(x.buy_item('Булава', 150))
# print(x.buy_item('Булава', 10))
# print(x.buy_item('Булава', 100))
#
# print(y.get_your_gold())
# print(y.buy_item('Меч', 100))
# print(y.buy_item('Меч', 500))


# Вариант из урока
# class GoblinMerchant:
#     def __init__(self, gold):
#         self.gold = gold
#
#     @staticmethod
#     def tax_rate():
#         return 0.1
#
#     @classmethod
#     def from_rich_merchant(cls):
#         return cls(1000)
#
#     def buy_item(self, item_name, item_price):
#         total_price = item_price + item_price * self.tax_rate()
#         if self.gold >= total_price:
#             self.gold -= total_price
#             return f"Куплен {item_name}"
#         else:
#             return "Недостаточно золота!"

'''Задание 3: Боец и маг Тема: Наследование.'''

'''1. Создайте базовый класс `Hero` с атрибутами:
    - `name` (имя героя).
    - `health` (здоровье).
    - Метод `take_damage`, который уменьшает здоровье на указанное значение.
2. Создайте два дочерних класса:
    - `Warrior` с методом `attack`, который возвращает "Нанёс 20 урона мечом".
    - `Mage` с методом `attack`, который возвращает "Нанёс 15 урона заклинанием".
3. Создайте объекты `Warrior` и `Mage` и вызовите их методы.'''

# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def take_damage(self, damage):
#         self.health -= damage
#         # return self.health
#         print(f'{self.name}, получил {damage}, здоровья осталось: {self.health}')
#
# class Warrior(Hero):
#     def attack(self):
#         return 'Нанёс 20 урона мечом'
#
# class Mage(Hero):
#     def attac(self):
#         return 'Нанёс 15 урона заклинанием'
#
# warrior = Warrior('Воин', 100)
# mage = Mage('Маг', 85)
#
# print(warrior.attack())
# print(mage.attac())

'''Задание 4: Задание на полиморфизм  '''

'''**Тема:** Полиморфизм.

1. Создайте классы `Peon` и `Knight`, которые:
    - Имеют метод `work`:
        - У `Peon` метод возвращает "Собирает золото".
        - У `Knight` метод возвращает "Сражается с врагами".
2. Напишите функцию `daily_work`, которая принимает объект героя и вызывает его метод `work`.
3. Протестируйте с обоими классами.'''

# class Peon:
#     def work(self):
#         return 'Собирает золото'
#
# class Knight(Peon):
#     def work(self):
#         return 'Сражается с врагами'
#
# # a = Knight()
# # print(a.work())
#
# def daily_work(a):
#     print(a.work())
#
# # daily_work(Knight())
#
# my_class = [Knight(), Peon()]
# for i in my_class:
#     daily_work(i)

'''Задание 5: Секретные артефакты Тема: Абстракция.'''

'''Абстракция.

1. Создайте абстрактный класс `Artifact` с абстрактным методом `activate`.
2. Создайте два класса:
    - `HealingArtifact`, метод `activate` возвращает: "Восстановлено 50 здоровья".
    - `DamageArtifact`, метод `activate` возвращает: "Нанесено 30 урона врагу".
3. Создайте объекты и вызовите метод `activate`.'''

# from abc import ABC, abstractmethod
#
# class Artifact(ABC):
#
#     @abstractmethod
#     def activate(self):
#         pass
#
# class HealingArtifact(Artifact):
#     def activate(self):
#         return 'Восстановлено 50 здоровья'
#
# class DamageArtifact(Artifact):
#     def activate(self):
#         return 'Нанесено 30 урона врагу'
#
# x = HealingArtifact()
# y = DamageArtifact()
#
# print(x.activate())
# print(y.activate())


'''Задание 6: Гоблинский банк  Тема: Инкапсуляция.'''

'''Гоблины открыли банк, где хранят золото своих клиентов. Вам нужно реализовать класс, 
который использует инкапсуляцию для управления золотом.

1. Создайте класс `GoblinBank`, который:
    - Имеет приватный атрибут `__gold`, содержащий количество золота у клиента.
    - В конструкторе принимает начальное количество золота и устанавливает его в `__gold`. 
    Если переданное значение отрицательное, выдает ошибку.
2. Реализуйте методы:
    - `get_gold()` — возвращает текущее количество золота.
    - `deposit_gold(amount)` — добавляет указанное количество золота, если оно больше 0.
    - `withdraw_gold(amount)` — уменьшает количество золота, если сумма не превышает доступное золото. 
    Если золота недостаточно, выводит сообщение: "Недостаточно золота!".
3. Протестируйте класс, создав объект и выполняя операции с золотом.'''

# class GoblinBank:
#     def __init__(self, gold):
#         self.__gold = gold
#         if self.__gold < 0:
#             raise ValueError ('gold < 0')
#
#     @property
#     def get_gold(self):
#         return self.__gold
#
#     # @gold.setter
#     def deposit_gold(self, amount):
#         if amount > 0:
#             self.__gold += amount
#             return self.__gold
#         else:
#             raise ValueError ('amount < 0')
#
#     # @gold.setter
#     def withdraw_gold(self, amount):
#         if amount <= self.__gold:
#             self.__gold -= amount
#             return self.__gold
#         else:
#             raise ValueError ('you want withdraw amount > deposit')
#
# bank = GoblinBank(100)
#
# try:
#     print(bank.get_gold)  # Вывод: 100
#     print(bank.deposit_gold(50))   # Вывод: Добавлено 50 золота. Текущий баланс: 150
#     print(bank.withdraw_gold(30))  # Вывод: Снято 30 золота. Текущий баланс: 120
#     print(bank.withdraw_gold(200)) # Вывод: Недостаточно золота!
# except ValueError as e:
#     print(f'Error {e}')




