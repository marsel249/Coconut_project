'''* Задание 1: Написать функцию greet(), которая не принимает никаких параметров и
выводит на экран сообщение "Hello, world!"'''

# def greet():
#     print('Hello, world!')
#
# greet()

'''* Задание 2: Написать функцию greet_user(name), которая принимает имя пользователя в качестве параметра 
и выводит приветствие вида "Привет, [имя]!" вызвать эту функцию несколько раз в коде с разными именами и 
сверить результат'''

import random
# name_list = ['Ivan', 'Serg', 'Viktor', 'Stas', 'Roman']
#
# def greet_user(name):
#     print(f'Привет, {name}!')

# print(random.choice(name_list))
# print(random.shuffle(name_list))
# greet_user(name_list[0])

# greet_user(random.choice(name_list))

'''* Задание 3: Написать функцию sum_numbers(a, b), которая принимает два числа в 
качестве параметров и выводит на экран их сумму'''

# num1 = 5
# num2 = 14
#
# def sum_numbers(a, b):
#     print(a + b)
#
# sum_numbers(num1, num2)

# #random
# numbers = [1, 2, 8, 19, 32, 11]
#
# def sum_numbers(a, b):
#     print(f'{a} + {b} = {a + b}')
#
# sum_numbers(random.choice(numbers), random.choice(numbers))

'''* Задание 4: Проверка на четность Написать функцию is_even(number), 
которая принимает целое число в качестве параметра и выводит на экран "Четное", 
если число четное, и "Нечетное", если число нечетное (Подсказка: используй оператор % для проверки остатка от деления)'''

# number = 11
#
# def is_even(number):
#     if number % 2 == 0:
#         print('Четное')
#     else:
#         print('Не четное')
#
# is_even(number)

# numbers = [1, 2, 4, 8, 16, 23, 42, 51]
#
# def is_even(number):
#     if number % 2 == 0:
#         print('Четное')
#     else:
#         print('Не четное')
#
# # for i in numbers:
# #     is_even(i)
#
# #Циклом, через индекс, пока список не кончится
# i = 0
# while i < len(numbers):
#     is_even(numbers[i])
#     i += 1

'''* Задание 5: (посложнее) Написать функцию rectangle_area(width, height), которая принимает ширину и высоту 
прямоугольника в качестве параметров. Функция должна проверять, что оба параметра являются положительными числами. 
Если хотя бы один из параметров не является положительным, функция должна вывести сообщение "Некорректные значения". 
В противном случае функция должна вычислить и вывести площадь прямоугольника'''

# a = 0
# b = 10
#
# def rectangle_area(width, height):
#     if width > 0 and height > 0:
#         print(f'S▯ = {a} * {b} = {a * b}')
#     else:
#         print('Некорректные значения')
#
# rectangle_area(a, b)


