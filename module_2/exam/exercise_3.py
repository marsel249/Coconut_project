# Задание 3 Массивы и другие структуры данных в Python

# Простые задания

# Работа со списком

'''Создайте список `fruits = ["apple", "banana", "cherry", "date"]`.

- Добавьте в список новый фрукт `"kiwi"`.
- Удалите фрукт `"banana"`.
- Выведите итоговый список.'''

# fruits = ["apple", "banana", "cherry", "date"]
# fruits.append('kiwi')
# fruits.remove('banana')
# print(fruits)

# Средние задания

# Работа с кортежем

'''- Создайте кортеж `numbers = (10, 20, 30, 40, 50)`.
- Выведите второй элемент кортежа.
- Попробуйте изменить значение третьего элемента и объясните результат.'''

# numbers = (10, 20, 30, 40, 50)
# print(numbers[1])
# numbers[2] = 300 #будет ошибка, кортеж не изменяемый тип данных
# print(numbers)

'''- Создайте множество `colors = {"red", "blue", "green"}`.
- Добавьте новый цвет `"yellow"`.
- Удалите цвет `"blue"`.
- Попробуйте добавить уже существующий цвет `"red"` и объясните результат.'''

# colors = {"red", "blue", "green"}
# print(colors)
# colors.add('yellow')
# print(colors)
# colors.remove('blue')
# print(colors)
# colors.add('red')
# print(colors) #Не изменяется

# Сложное задание

# Работа с диапазоном и списками

'''- Создайте диапазон чисел от `1` до `20` включительно.
- Преобразуйте его в список.
- Найдите сумму всех чисел в списке.
- Найдите все числа, которые делятся на `3`, и создайте из них новый список.
- Выведите оба списка: оригинальный и новый.'''

# my_list = []
# for i in range(1,21):
#     my_list.append(i)
# print(my_list)
# print(sum(my_list))
#
# new_my_list = []
# for i in my_list:
#     if i%3 == 0:
#         new_my_list.append(i)
# print(new_my_list)


# # Создаём диапазон
# num_range = range(1, 21)
#
# # Преобразуем в список
# num_list = list(num_range)
#
# # Находим сумму всех чисел
# total_sum = sum(num_list)
#
# # Числа, делящиеся на 3
# divisible_by_3 = [num for num in num_list if num % 3 == 0]
#
# print("Оригинальный список:", num_list)
# print("Сумма чисел:", total_sum)
# print("Числа, делящиеся на 3:", divisible_by_3)


