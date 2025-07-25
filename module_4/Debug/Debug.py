# a = 1
# b = 10
#
# def calc1(*args, **kwargs):
#     return a + b
#
# def calc2(*args, **kwargs):
#     return a - b
#
# print(calc1(a, b)) #После выполнения этой функции, остановка на дебаг
# print(calc2(a, b))

# def calculate_sum(a, b):
#     result = a + b  # Точка остановки здесь
#     return result
#
# x = 5
# y = 10
# total = calculate_sum(x, y)
# print(total)

'''step over'''
# def inner_function(x):
#     return x * 2
#
# def outer_function(a):
#     b = inner_function(a + 1)  # Step Over здесь
#     c = b * 3                # После Step Over выполнение будет здесь
#     return c
#
# result = outer_function(5)
# print(result)

'''Step Into'''

# def inner_function(x):
#     return x * 2
#
# def outer_function(a):
#     b = inner_function(a + 1)  # Step Over здесь
#     c = b * 3                # После Step Over выполнение будет здесь
#     return c
#
# result = outer_function(5)
# print(result)

# def func1(x): return x + 1
# def func2(x): return x * 2
# def func3(x): return x**2
#
# result = func1(func2(func3(2))) # Тут несколько вызовов
#
# print(result)

'''Step Into My Code '''

# import requests  # Сторонняя библиотека
#
# def my_function(url):
#     response = requests.get(url)  # Step Into My Code здесь
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "Error"
#
# url = "https://www.example.com"
# content = my_function(url)
# print(content)

'''step out'''

# def inner_function(x):
#     return x * 2  # Step Out здесь
#
# def outer_function(a):
#     b = inner_function(a + 1)  # Step Into здесь
#     c = b * 3
#     return c
#
# result = outer_function(5)
# print(result)

'''Run to Cursor'''

# import requests  # Сторонняя библиотека
#
# def my_function(url):
#     response = requests.get(url)  # брейкпоинт сюда
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "Error"
#
# url = "https://www.example.com"
# content = my_function(url)
# i = "i'm here"
# print(content)

'''practice YouTube'''

def one(x, y):
    result = x + y
    return two(result)

def two(result):
    result = f'{result}!!'
    return three(result)

def three(result):
     return 100 / result.count('!')

def cycle(value):
    even_squares = [e ** 2 for e in range(10) if e % 2 == 0]
    for e in range(6):
        value += e
        print(value)
    return value

if __name__ == '__main__':
    print(one(1, 2))
    cycle(50)


