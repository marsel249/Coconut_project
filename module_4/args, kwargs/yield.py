
# def generate_numbers():
#     for i in range(5):
#         yield i  # Возвращает значение и приостанавливает выполнение
#
# gen = generate_numbers()
# print(next(gen))  # Выводит: 0
# print('print между yield')
# print(next(gen))  # Выводит: 1
# print(next(gen))  # Выводит: 2
# print(next(gen))  # Выводит: 3
# print(next(gen))  # Выводит: 4
# # print(next(gen))  # Выводит: Error



# def squares(n):
#     for i in range(n):
#         yield i ** 2
#
# for square in squares(5):
#     print(square)  # Выводит квадраты чисел от 0 до 4


# import pytest
#
# @pytest.fixture
# def db_connection():
#     # Установка соединения
#     connection = "Подключение к БД"
#     yield connection  # Передача соединения в тест
#     # Очистка ресурсов после теста
#     print("Закрытие соединения")
#
# def test_example(db_connection):
#     assert db_connection == "Подключение к БД"

