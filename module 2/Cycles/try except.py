# numbers = [10, 0, 5, 2]
#
# for num in numbers:
#     try:
#         result = 10 / num
#         print(f"Результат деления: {result}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно.")

# data = ["123", "abc", "456", None]
#
# for item in data:
#     try:
#         number = int(item)  # Попытка преобразования строки в число
#         print(f"Число: {number}")
#     except (ValueError, TypeError):
#         print(f"Ошибка: {item} не удалось преобразовать в число.")


# operations = [(10, 2), (5, 0), (8, "string"), (4, 2)]
#
# for a, b in operations:
#     try:
#         result = a / b
#         print(f"Результат: {result}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно.")
#     except TypeError:
#         print(f"Ошибка: Неверный тип данных: {b}")

'''
1. Напишите цикл, который делит число 100 на элементы списка `[10, 0, 5, "abc", 2]`.
Обработайте ошибки деления на ноль и преобразования типов.
2. Реализуйте цикл, который читает числа из списка и обрабатывает ошибки для значений,
которые нельзя преобразовать в числа (например, `["123", "text", None, "456"]`).
3. Напишите программу, которая выполняет операции с числами в парах (например, `[ (10, 5), (3, 0), (7, "str") ]`),
обрабатывая деление на ноль и ошибки типов данных.'''

# my_list = [10, 0, 5, "abc", 2]
# for i in my_list:
#     try:
#         result = 100/i
#         print(result)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя")
#     except TypeError:
#         print('Неверный тип данных')

# my_list = ["123", "text", None, "456"]
# print('data\ttype\ttype_NOW')
# for i in my_list:
#     try:
#         result = int(i)
#         print(result, type(i), type(result))
#     except (TypeError, ValueError):
#         print('Как-то не удалось')

# my_list = [ (10, 5), (3, 0), (7, "str") ]
# for a,b in my_list:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя")
#     except TypeError:
#         print('Неверный тип данных')



