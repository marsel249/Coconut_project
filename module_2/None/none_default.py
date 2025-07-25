'''- **Задание #1**
    1. Напишите функцию `calculate_discount(price, discount=None)`.
    2. Если `discount` равно `None`, установите его значение на `0.05` (5%).
    3. Функция должна возвращать цену с учетом скидки.
    4. Проверьте функцию с `discount` и без него.
- **Задание #2**
    1. Создайте функцию `add_to_list(item, my_list=None)`, которая добавляет элемент `item` в список `my_list`.
    2. Если `my_list` равно `None`, создайте внутри функции новый пустой список.
    3. Функция должна возвращать обновленный список.
    4. Протестируйте функцию, вызывая её без списка и с существующим списком.
- **Задание #3**
    1. Напишите функцию `send_email(subject, body, recipient=None)`.
    2. Если `recipient` равно `None`, установите его значение на `"support@example.com"`.
    3. Функция должна выводить сообщение с темой, телом письма и получателем.
    4. Протестируйте функцию, передавая `recipient` и оставляя его пустым.'''

# def calculate_discount(price, discount=None):
#     if discount is None:
#         discount = 1 - 0.05
#         print(discount * price)
#     else:
#         print(discount * price)
#
# calculate_discount(100, 0.5)

# def add_to_list(item, my_list=None):
#     if my_list is None:
#         my_list = []
#         my_list.append(item)
#         print(my_list)
#     else:
#         my_list.append(item)
#         print(my_list)
#
# new_list = [1, 2, '123457', True]
# add_to_list(18, new_list)

# def send_email(subject, body, recipient=None):
#     if recipient is None:
#         recipient = 'support@example.com'
#         print(subject, body, recipient)
#     else:
#         print(subject, body, recipient)
#
# send_email('объект', 'тело', 'суппорт')