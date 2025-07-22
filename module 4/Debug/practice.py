'''Упражнение 1: Step Over и Step Into

1. Установите брейкпоинт на строке `processed_data = transform_data(data)`
2. Запустите отладку
3. Используйте Step Over (F8), чтобы выполнить строку и перейти к следующей
4. Снова установите брейпоинт на ту же строку
5. Запустите отладку
6. Используйте Step Into (F7), чтобы "войти" внутрь функции `transform_data`
7. Используйте Step Over внутри `transform_data`, чтобы выполнить каждую строку
8. Используйте Step Out (Shift+F8), чтобы вернуться в функцию `process_data`'''

# def process_data(data):
#     processed_data = transform_data(data)
#     result = calculate_result(processed_data)
#     return result
#
# def transform_data(data):
#     return [x * 2 for x in data]
#
# def calculate_result(data):
#     return sum(data)
#
# data = [1, 2, 3]
# final_result = process_data(data)
# print(final_result)

'''Упражнение 2: Step Out и просмотр переменных

1. Установите точку останова на строке `d = c * 2`
2. Запустите отладку
3. Посмотрите значения `a`, `b`, `c` в окне *Variables*
4. Используйте Step Out
5. Посмотрите значения `x`, `y`, `z` в окне *Variables*'''

# def inner(a, b):
#     c = a + b
#     d = c * 2 # Поставьте тут точку останова
#     return d
#
# def outer(x):
#     y = 10
#     z = inner(x, y)
#     return z
#
# result = outer(5)
# print(result)

'''Упражнение 3: Smart Step Into

1. Установите точку останова на строке `result = a(b(c(2)))`.
2. Запустите отладку.
3. Нажмите Shift + Alt + F7 (Smart Step Into).
4. Выберите функцию `c` для входа.
5. Повторите шаги 3 и 4, выбирая функции `b` и `a` по очереди.

Эти упражнения помогут вам лучше понять, 
как работают команды пошагового выполнения и как использовать их для эффективной отладки кода в PyCharm'''

def a(x): print("a"); return x + 1
def b(x): print("b"); return x * 2
def c(x): print("c"); return x ** 2

result = a(b(c(2))) # Поставьте тут точку останова
print(result)