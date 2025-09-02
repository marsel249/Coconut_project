'''Учимся делать декораторы'''

# #Без декоратора
# def my_decorator(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#
#     return wrapper()
#
# def say_hello():
#     print('Hello!!11 withOUT decorator')
#
# my_decorator(say_hello)
#
# #Декоратор
# @my_decorator
# def say_hello():
#     print('Hello!!11 with decorator')
#
# say_hello
import time


#____________
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         func(*args, **kwargs)
#         print('after')
#
#     return wrapper

#Декоратор
# @my_decorator
# def say_hello(name):
#     print(f'Hello!!11 with decorator, name: {name}')
#
# say_hello(name='Sherlock')
#____________
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before')
#         reasult = func(*args, **kwargs)
#         print('after')
#         return reasult
#
#     return wrapper
#
# @my_decorator
# def add_number(a, b):
#     print(f'Add numbers a, b') #{a} + {b} = {a+b}
#     return a + b
#
# resault = add_number(5, 10)
# print(resault)
#____________

'''Декоратор из урока'''
# import time
#
#
# def my_new_decorator_retry(func):
#     def wrapper_time_retry(*args, **kwargs):
#         retry_seconds = [3, 5, 7]
#         for seconds in retry_seconds:
#             try:
#                 return func(*args, **kwargs)
#             except ZeroDivisionError as e:
#                 print(f'Error, {e}, retry in {seconds} seconds')
#                 time.sleep(seconds)
#         #return func(*args, **kwargs)
#     return wrapper_time_retry
#
# @my_new_decorator_retry
# def math_ab(a, b):
#     print(f'Try {a} / {b}')
#     return a / b
#
# math_ab(5, 0)


#______

# def add_text(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper
#
# @add_text
# def something():
#     print('my_original_func')
#
# something()
#
# # # Тоже самое, что и с декоратором @
# # something = add_text(something)
# # something()

#_____

def add_logs(func):
    def wrapper(*args):
        print(f'start {func.__name__}')
        func(*args)
        print(f'finish {func.__name__}')
    return wrapper

@add_logs
def something(x):
    print(x * 2)

something(4)



#____________
'''Методы класса из курса'''

# class Dog:
#     species = "Canis familiaris"  # Атрибут класса
#
#     @classmethod
#     def get_species(cls):  # cls ссылается на класс Dog
#         return cls.species
#
# print(Dog.get_species())

# Метод класса может быть вызван напрямую через класс
# class Example:
#     @classmethod
#     def method(cls):
#         print(f"This is a method of {cls}.")
#
# Example.method()  # Вывод: This is a method of <class '__main__.Example'>.
# print(Example)    # Вывод: <class '__main__.Example'>.

# Методы класса также можно вызывать через объект.
# В этом случае Python автоматически передает класс объекта в качестве аргумента cls
# class Example:
#     @classmethod
#     def method(cls):
#         print(f"This is a method of {cls}.")
#
# obj = Example()
# obj.method()  # Вывод: This is a method of <class '__main__.Example'>.
#____________

# class Cat:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Cat.count += 1  # Увеличиваем счетчик при создании объекта
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# cat1 = Cat("Barsik")
# cat2 = Cat("Murzik")
# cat3 = Cat("Pushok")
#
# print(Cat.get_count())      # Вывод: 3
# print(cat1.get_count())    #Вывод: 3