'''**kwargs'''

# def greed(**kwargs):
#     print(f'Hello, {kwargs['name']}! You are {kwargs['age']} years old.')
#
# greed(name='Alice', age=25)

# def something(**kwargs):
#     for key, value in kwargs.items():
#         print(f'key: {key}, value: {value}')
#
#
# create_dict(name='Alice', age=25, name1='Alice1', age1=30)

# def create_dict(**kwargs):
#     return kwargs
#     # for key, value in kwargs.items():
#     #     my_dict = {key:value}
#
# print(create_dict(a=1, b=2, c=3))
# # Вывод: {'a': 1, 'b': 2, 'c': 3}

# def update_settings(name_file, **kwargs):
#     name_file.update(kwargs)
#     return name_file
#
# default_settings = {"theme": "light", "notifications": True}
# print(update_settings(default_settings, theme="dark", volume=80))
# # Вывод: {'theme': 'dark', 'notifications': True, 'volume': 80}

# def filter_kwargs(**kwargs):
#     my_dict = dict()
#     for key, value in kwargs.items():
#         if value > 10:
#             x = {key:value}
#             my_dict.update(x)
#     return my_dict
#
# print(filter_kwargs(a=5, b=20, c=15, d=3))
# # Вывод: {'b': 20, 'c': 15}

'''Декоратор'''
# def log_kwargs(func):
#     def wrapper(*args, **kwargs):
#         print(f'Called with kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log_kwargs
# def my_function(a, b, **kwargs):
#     return a + b
#
# my_function(5, 10, debug=True, verbose=False)
# # Вывод:
# # Called with kwargs: {'debug': True, 'verbose': False}

'''Пример создания простого декоратора'''
# # 1. Создаём декоратор
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Функция {func.__name__} вызвана")  # Добавляем логирование
#         return func(*args, **kwargs)  # Вызываем оригинальную функцию
#     return wrapper
#
# # 2. Применяем декоратор к функции
# @log_decorator
# def greet(name):
#     print(f"Привет, {name}!")
#
# # 3. Вызываем функцию
# greet("Анна")

'''*args'''

# def add_numbers(*args):
#     return sum(args)
#
# print(add_numbers(1, 2, 3))  # 6
# print(add_numbers(10, 20, 30, 40))  # 100

# def create_list(*args):
#     my_list = []
#     for i in args:
#         my_list.append(i)
#     return my_list
#
# print(create_list(1, "apple", True, 3.14))  # [1, "apple", True, 3.14]


# def pass_arguments(*args):
#     print_args(*args)
#
# def print_args(*args):
#     for arg in args:
#         print(arg)
#
# pass_arguments("Hello", 42, False)
# # Вывод:
# # Hello
# # 42
# # False

# def find_max(*args):
#     return max(args)
#
# print(find_max(10, 20, 5, 100, 50))  # 100

# def join_strings(*args):
#     return ' '.join(args)
#
# print(join_strings("Hello", "world", "!"))  # "Hello world !"

# def process_data(*args, **kwargs):
#     print(f'Positional arguments: {args}')
#     print(f'Keyword arguments: {kwargs}')
#
#
# process_data(1, 2, 3, name="Alice", age=25)
# # Вывод:
# # Positional arguments: (1, 2, 3)
# # Keyword arguments: {'name': 'Alice', 'age': 25}

# def configure_function(*args, **kwargs):
#     my_dict = dict()
#     for i in args:
#         x = {i : None}
#         my_dict.update(x)
#     my_dict.update(kwargs)
#     return my_dict
#
# print(configure_function("theme", "volume", theme="dark", volume=50))
# # Вывод: {'theme': 'dark', 'volume': 50}

# def log_args_kwargs(func):
#    def wrapper(*args, **kwargs):
#         print(f'Вывод: \nPositional arguments: {args}\nKeyword arguments: {kwargs}')
#         return func(*args, **kwargs)
#    return wrapper
#
#
# @log_args_kwargs
# def my_function(x, y, **kwargs):
#     return x + y
#
# my_function(10, 20, debug=True, verbose=False)
# # Вывод:
# # Positional arguments: (10, 20)
# # Keyword arguments: {'debug': True, 'verbose': False}