'''*args, числа'''
from tkinter.font import names

# def sum_all(*args):
#     summ = 0
#     for i in args:
#         summ += i
#     return summ
#
# print(sum_all(1, 2, 4, 8)) #Складываем аргументы, переданные в функцию
# print(type(sum_all(1, 2, 4, 8))) #int
#
#
#
# a = [1, 2, 5, 10, 2]
# b = [15, 2, 13]
#
# print(sum_all(*a, *b)) # Сложение списков с помощью функции sum_all, через *args
# print(sum(a) + sum(b)) # Сложение списков с помощью функции sum

'''**kwargs'''
# def kwargs_func(**kwargs):
#     print(kwargs)
#     print((type(kwargs)))
#
# kwargs_func(name='lalala', age=30, status=True) #return dict

# def kwargs_func(**kwargs):
#     # print(kwargs)
#     print((type(kwargs)))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)

# kwargs_func(name='lalala', age=30, status=True) #return dict

#_________
#Как положить словарь в функцию

# def kwargs_func(**kwargs):
#     # print(kwargs)
#     print((type(kwargs)))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
# my_dict = {
#     'name':'lalala',
#     'age':30,
#     'status':True
# }
#
# kwargs_func(**my_dict) #return dict
#_________



