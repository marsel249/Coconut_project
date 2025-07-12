# Задание 2 Манипуляции над типами данных

# Простые задания

# Манипуляции над строками (методы строк)

'''- Напишите программу, которая:
    - Создаёт строку `text = "Python is awesome!"`.
    - Применяет к этой строке метод `upper()` и выводит результат.
    - Применяет метод `replace()` для замены слова `awesome` на `amazing` и выводит результат.'''


# text = "Python is awesome!"
#
# print(text.upper())
# print(text.replace('awesome','amazing'))

'''- Напишите программу, которая:
    - Создаёт строку `text = "Hello, Python!"`.
    - Выводит первые 5 символов строки.
    - Выводит все символы строки через один.'''

# text = 'Hello, Python!'
# print(text[0:6])
# print(text[::2])

'''Напишите программу, которая:

1. Создаёт число `pi = 3.14159`.
2. Округляет его до двух знаков после запятой.
3. Выводит результат.'''

# pi = 3.14159
# print(f'{pi:.2f}')
# print(round(pi, 2))

# Средние задания

# Замена подстрок

'''- Напишите программу, которая:
    - Создаёт строку `quote = "Python is easy and powerful!"`.
    - Заменяет `easy` на `fun` и `powerful` на `versatile`.
    - Выводит результат.'''

# quote = "Python is easy and powerful!"
# new_quote = quote.replace('easy', 'fun')
# really_new_quote = new_quote.replace('powerful', 'versatite')
# print(really_new_quote)
#
# new_quote = quote.replace("easy", "fun").replace("powerful", "versatile")
# print("Изменённая строка:", new_quote)

# Задания с f"строкой"

'''- Напишите программу, которая:
    - Создаёт переменные `name = "Alice"` и `age = 25`.
    - Формирует строку вида: `Alice is 25 years old.` с помощью f-строки и выводит её.'''

# name = "Alice"
# age = 25
# print(f'{name} is {age} years old')

'''**Обработка строки и числа вместе**
    - Напишите программу, которая:
        - Создаёт строку `data = "Price: 1234.5678 USD"`.
        - Извлекает числовую часть строки (1234.5678) с помощью среза и преобразует её в число.
        - Округляет это число до двух знаков после запятой.
        - Формирует новую строку вида: `"Rounded price: 1234.57 USD"` и выводит её.'''


# data = "Price: 1234.5678 USD"
# slice_data = data[7:17]
# int_data = float(slice_data)
# newdata = round(int_data, 2)
# print(f'Rounded price: {newdata} USD')
