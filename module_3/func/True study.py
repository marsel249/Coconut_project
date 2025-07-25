'''* Задание 1 (easy): Калькулятор стоимости доставки
Написать функцию calculate_delivery_cost(weight, distance, fragile=False),
которая рассчитывает стоимость доставки посылки.
    * weight (число): вес посылки в кг.
    * distance (число): расстояние доставки в км.
    * fragile (булево, по умолчанию False): является ли посылка хрупкой.
* Правила расчета:
    * Базовая стоимость: 10 рублей за кг + 5 рублей за км.
    * Если посылка хрупкая, стоимость увеличивается на 50%.
    * Минимальная стоимость доставки: 200 рублей.
* Функция должна возвращать стоимость доставки
'''


'''Мой вариант'''

# def calculate_delivery_cost(weight, distance, fragile=False):
#     if fragile is True: #Нейросеть: True избыточной, можно убрать, есть проверка на истинность
#         result = (weight * 10 + 5 * distance) * 1.5
#         if result >= 200:
#             print(f'Стоимость доставки: {result} рублей')
#         else:
#             print('Стоимость доставки меньше 200 рублей')
#     else:
#         result = (weight * 10 + 5 * distance)
#         if result >= 200:
#             print(f'Стоимость доставки: {result} рублей')
#         else:
#             print('Стоимость доставки меньше 200 рублей')
#
# try:
#     weight = int(input('Вес: '))
#     distance = int(input('Расстояние: '))
#     fragile = int(input('Хрупкое? Если - да, напиши "1", если нет - "0, или, что угодно"'))
#     if fragile == 1:
#         fragile = True
#     else:
#         fragile = False
#
#     calculate_delivery_cost(weight, distance, fragile)
# except(ValueError, TypeError):
#     print('Error?')
# except Exception as e:
#     print(f'Произошла ошибка: {e}')

'''Вариант нейросети'''

# def calculate_delivery_cost(weight, distance, fragile=False):
#     base_cost = weight * 10 + 5 * distance
#     if fragile:
#         base_cost *= 1.5
#
#     if base_cost >= 200:
#         print(f'Стоимость доставки: {base_cost} рублей')
#     else:
#         print('Стоимость доставки меньше 200 рублей')
#
#
# try:
#     weight = int(input('Вес (кг): '))
#     distance = int(input('Расстояние (км): '))
#     fragile_input = input('Хрупкое? (да/нет): ').lower()
#     fragile = fragile_input == 'да'  # True, если введено "да"
#
#     calculate_delivery_cost(weight, distance, fragile)
# except ValueError:
#     print('Ошибка: введите число для веса и расстояния!')
# except Exception as e:
#     print(f'Произошла ошибка: {e}')


'''Напишите функцию `analyze_numbers(numbers)`, которая принимает **список** чисел и возвращает словарь со следующей информацией:

- `"average"`: среднее значение чисел в списке.
- `"min"`: минимальное число в списке.
- `"max"`: максимальное число в списке.
- `"even_count"`: количество четных чисел в списке

Если список пустой, функция должна вернуть словарь со значениями `None` для всех ключей'''

'''Мой вариант (Не реализовал проверку на None)'''
# my_list = [1, 2, 3, 8, 15, 32, 4]
# my_list = []

# def analyze_numbers(numbers=None):
#     min_list = min(numbers)
#     max_list = max(numbers)
#     average = round(sum(numbers)/len(numbers), 2)
#     # even_count = 0
#     even_list = []
#     for i in numbers:
#         if i % 2 == 0:
#             even_list.append(i)
#             even_count = len(even_list)
#     print({'average':{average}, 'min':{min_list}, 'max':{max_list}, 'even_count':{even_count}})
#
# analyze_numbers(my_list)

'''Версия нейросети'''


# def analyze_numbers(numbers):
#     if not numbers:  # если список пустой
#         return {
#             "average": None,
#             "min": None,
#             "max": None,
#             "even_count": None
#         }
#
#     return {
#         "average": sum(numbers) / len(numbers),
#         "min": min(numbers),
#         "max": max(numbers),
#         "even_count": sum(1 for num in numbers if num % 2 == 0)
#     }
#
#
# # Тестирование
# my_list = [1, 2, 3, 8, 15, 32, 4]
# print(analyze_numbers(my_list))  # {'average': 9.285..., 'min': 1, 'max': 32, 'even_count': 4}
#
# empty_list = []
# print(analyze_numbers(empty_list))  # {'average': None, 'min': None, 'max': None, 'even_count': None}
#
# analyze_numbers(my_list)


'''* Задание 3 (medium): Фильтрация списка по условию
Напишите функцию filter_list(data, threshold), которая принимает список чисел data и число threshold в качестве аргументов. 
Функция должна вернуть новый список, содержащий только те числа из data, которые больше или равны threshold.'''

# my_list = [1, 2, 3, 8, 15, 32, 4]
# number = 7
#
# def filter_list(data, threshold):
#     numbers = []
#     for i in data:
#         if i >= threshold:
#             numbers.append(i)
#     return numbers
#
# print(filter_list(my_list, number))



# print(1)
# print(1,2)
# print(1,2,3)
# print(1,2,3,4)
# print(1,2,3,4,5)

# print(sum(range(1,21)))

# def say_hello():
#     print('Salam!')
# say_hello()

# def print_stars():
#     print('*****')
# print_stars()

# def print_line():
#     print(f'{20 * "-"}')
# print_line()

# def goodbye():
#     print('Инвертированный салам!')
# goodbye()

#_________________

# my_name = 'Sherlock'
# def get_my_name(name):
#     return name

# print(get_my_name(my_name))

# my_name_def = get_my_name(my_name)
# print(my_name_def)

# def get_lucky_number():
#     return 7
#
# print(get_lucky_number())

# def get_greeting():
#     return 'Welcome epta'
#
# print(get_greeting())

#_________________

# def print_even_numbers():
#     for i in range(2,11):
#         if i % 2 == 0:
#             print(i)
#
# print_even_numbers()

# def print_countdown():
#     # for i in range(5, 0, -1):
#     #     print(i)
#
#     # n = 5
#     # while n > 0:
#     #     print(n)
#     #     n -= 1
#
# print_countdown()

# def print_alphabet():
#     print('A', 'B', 'C', 'D', 'E')
#
# print_alphabet()

# def print_multiplication_table():
#     for i in range(1, 6):
#         print(f'{i} * 2 = {i * 2}')
#
# print_multiplication_table()

# def print_triangle():
#     for i in range(1,6):
#         print(i * '*')
#
# print_triangle()

#_________________

# def sum_first_ten():
#     return sum(range(1, 11))
#
# print(sum_first_ten())

# my_word = 'hellooo'
# def count_vowels_in_hello(word):
#     exceptions = 'AEIOUYaeiouy'
#     count = 0
#     for i in word:
#         if i in exceptions:
#             count +=1
#     return count
#
# print(count_vowels_in_hello(my_word))

# my_list = [1, 5, 3, 9, 2]
# # print(max(my_list))
# def get_max_from_list(data):
#     return max(data)
#
# print(get_max_from_list(my_list))

# a = 4
# def calculate_area_of_square(data):
#     return data ** 2
#
# print(calculate_area_of_square(a))

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def get_length_of_alphabet(data):
#     return len(data)
#
# print(get_length_of_alphabet(alphabet))
#_________________

import random

# random_name = ['ivan', 'igor', 'viktor']
#
# def greet(name):
#     return f'salam! {random.choice(name)}'
#
# print(greet(random_name))

# x = int(input('Введи число: '))
# def print_number(num):
#     print(f'Вы ввели: {num}')
#
# print_number(x)

# my_word = 'Salam ' #костыль в виде пробела, нужно править ф строкой
# def repeat_word(word):
#     print(f'{word * 3}')
#
# repeat_word(my_word)

# my_word = 'lalalalala'
# def print_length(text):
#     print(len(text))
#
# print_length(my_word)

# number = 50
# def print_double(number):
#     print(number*2)
#
# print_double(number)

# my_number = 50
# def add_ten(number):
#     print(number + 10)
#
# add_ten(my_number)

# my_number = 50
# def multiply_by_three(num):
#     print(num * 3)
#
# multiply_by_three(my_number)

# my_number = 13
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(my_number))

#_________________
# n = 15
# def print_range(n):
#     for i in range(1,n+1):
#         print(i)
#
# print_range(n)

# n = 10
# def print_stars(count):
#     print(n*'*')
#
# print_stars(n)

# n = 10
# def print_table(num):
#     for i in range(1, 6):
#         print(f'{num} * {i} = {i * num}')
#
# print_table(n)

# n = -3
# def analyze_number(num):
#     if num > 0:
#         return 'Положительное'
#     elif num < 0:
#         return 'Отрицательное'
#     return 'is - 0'
#
# print(analyze_number(n))

# n = 100
# def count_digits(number):
#     return len(str(number))
#
# print(count_digits(n))

# number = 10
# def sum_to_n(n):
#     result = 0
#     for i in range(1, n+1):
#         result += i
#     return result
#
# print(sum_to_n(number))

# x = [55, 71, 82, 93]
# y = random.choice(x)
# # print(y)
# def get_grade(score):
#     if score >= 90:
#         return f'{score} - A'
#     elif score >= 80 < 90:
#         return f'{score} - B'
#     elif score >=70 < 80:
#         return f'{score} - C'
#     else:
#         return f'{score} - F'
# print(get_grade(y))
#_________________

# a = 'Ivan'
# b = 'Ivanov'
# c = '' #'Ivanovich'
#
# def greet_person(first_name, last_name, second_name=None):
#     if second_name is not None:
#         return f'Salam, {first_name} {last_name} {second_name}'
#     else:
#         return f'Salam, {first_name} {last_name}'
#
# print(greet_person(a, b, c))

# def compare_numbers(a, b):
#     if a > b:
#         return f'{a} > {b}'
#     else:
#         return f'{a} < {b}'
# a = 18
# b = 12
#
# print(compare_numbers(a,b))

# def print_info(name, age, city):
#     print(f'name: {name},\nage: {age},\ncity: {city}')
#
# print_info('igor',37,'sochi')

# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(10, 15))

# def get_full_name(first, last):
#     return f'{first} {last}'
#
# print(get_full_name('Ivan','Ivanov'))

# a = 10
# b = 15
#
# def calculate_area(length, width):
#     return a * b
#
# print(calculate_area(a, b))

# a = 1
# b = 2
# c = 15
#
# def find_max(a, b, c):
#     list_max = [a, b, c]
#     return max(list_max)
#
# print(find_max(a, b, c))
#_________________
# number = 10
#
# def double(x):
#     return x * 2
#
# def print_double_result(num):
#     print(double(num))
#
# print_double_result(number)

# def get_square(x):
#     return x ** 2
#
# def sum_of_squares(a, b):
#     return get_square(a) + get_square(b)
#
# print(sum_of_squares(5, 10))

# def get_length(text):
#     return len(text)
#
# def compare_lengths(text1, text2):
#     if get_length(text1) > get_length(text2):
#         return f'{text1} > {text2}'
#     elif get_length(text1) == get_length(text2):
#         return f'{text1} = {text2}'
#     else:
#         return f'{text1} < {text2}'
#
# print(compare_lengths('lalalal','lalalal'))

# def celsius_to_fahrenheit(c):
#     return c * 9/5 +32
#
# # print(celsius_to_fahrenheit(10))
# def compare_temperatures(c1, c2):
#     if celsius_to_fahrenheit(c1) > celsius_to_fahrenheit(c2):
#         return f'{celsius_to_fahrenheit(c1)} > {celsius_to_fahrenheit(c2)}'
#     elif celsius_to_fahrenheit(c1) == celsius_to_fahrenheit(c2):
#         return f'{celsius_to_fahrenheit(c1)} = {celsius_to_fahrenheit(c2)}'
#     else:
#         return f'{celsius_to_fahrenheit(c1)} < {celsius_to_fahrenheit(c2)}'
#
# print(compare_temperatures(10, 10))

# def add_ten(x):
#     return x + 10
#
# def process_numbers(a, b):
#     return add_ten(a) + add_ten(b)
#
# print(process_numbers(20, 30))

# def multiply_by_two(x):
#     return x * 2
#
# def calculate_perimeter(length, width):
#     return multiply_by_two(length) + multiply_by_two(width)
#
# print(calculate_perimeter(5, 10))

# def is_even(x):
#     if x % 2 == 0:
#         return int(x)
#     else:
#         return False
#
# def filter_even_sum(a, b, c):
#     return is_even(a) + is_even(b) + is_even(c)
#
# # print(filter_even_sum(1,2,4), type(filter_even_sum(1,2,4)))
# # print(is_even(2), type(is_even(2)))
#
# x = 11
# y = 15
# z = 21
#
# print(filter_even_sum(x,y,z))

#_________________

# def inner_function():
#     print('Внутренняя функция')
#
# def outer_function():
#     inner_function()
#
# outer_function()

# def outer_function():
#     def inner_function():
#         print("Внутренняя функция")
#
#     inner_function()
# outer_function()

# def outer_function():
#     def inner_function():
#         print("Внутренняя функция")
#
#     return inner_function
#
# inner = outer_function()
#
# inner()


# def number_analyzer(num):
#     def is_positive(num):
#         if num > 0:
#             return f'{num} Положительное'
#         elif num < 0:
#             return f'{num} Отрицательное'
#         else:
#             return f'{num} = 0'
#
#     def is_even(num):
#         if num % 2 == 0:
#             return f'{num} Четное'
#         else:
#             return f'{num} Не четное'
#
#     return is_positive(num), is_even(num)
#
# print(number_analyzer(0))
