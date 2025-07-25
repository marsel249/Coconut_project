# try:
#     value = int(input("Введите число: "))  # Попытка преобразовать ввод пользователя в число
#     result = 10 / value
# except ValueError:  # Если введено не число
#     print("Ошибка: нужно вводить только числа!")
# except ZeroDivisionError:  # Деление на ноль
#     print("Ошибка: деление на ноль!")
# except Exception as e:  # Общее исключение для любых других ошибок
#     print("Произошла ошибка:", e)
# else:  # Блок выполнится, если исключений не было
#     print(f"Результат: {result}")
# finally:  # Этот блок выполнится в любом случае
#     print("Завершение программы.")


# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("На ноль делить нельзя!")  # Генерируем исключение
#     return a / b
#
# try:
#     print(divide(10, 0))
# except ZeroDivisionError as e:
#     print("Ошибка:", e)

'''Задача: Написать функцию для деления двух чисел с обработкой исключений.'''

# a = 4
# b = 6
#
# def safe_divide(a, b):
#     try:
#         print(a / b)
#     except (ZeroDivisionError, TypeError) as e:
#         print(f'Error {e}')
#     else:
#         print('Без ошибок')
#     finally:
#         print('Завершение')
# safe_divide(a, b)

'''* Задача 2: Проверка ввода и чтение файла 
Описание:
    1. Напишите функцию, которая принимает имя файла и читает из него содержимое.
    2. Если файл не существует, программа должна сообщить об ошибке.
    3. Если введенное имя файла пустое, программа должна сообщить, что имя файла не может быть пустым.'''


# def read_file(filename):
#
#     try:
#         if not filename:
#             return print(f'Имя файла пустое')
#         with open(filename, 'r', encoding='utf-8') as file:
#             print(file.read())
#     except FileNotFoundError as e:
#         print(f'Error: {e}')
#     else:
#         print('Файл прочитан')
#     finally:
#         print('Directed by \nRobert B. Weide')

# read_file('name_file')
# read_file('')

'''1. Напишите функцию, которая принимает список чисел и делит 100 на каждое число из списка.
2. Обработайте следующие ошибки:
    - Деление на ноль.
    - Некорректный тип данных в списке.
3. Функция должна пропустить проблемные элементы и продолжить выполнение.'''

# my_list = [1, 8 , 19, 0, 84, 100, 1500]
#
# def divide_numbers(numbers):
#     for num in numbers:
#         try:
#             if num == 0:
#                 raise ZeroDivisionError('на 0 делить нельзя')
#             result = 100 / num
#             print(result)
#         except (ZeroDivisionError, TypeError) as e:
#             print(f'Error: {e}')
#
# divide_numbers(my_list)















