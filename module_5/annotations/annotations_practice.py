# def multiply(a: int, b: int) -> int:
#     return a * b
#
# print(multiply(5, 'd'))

# def sum_numbers(numbers: list[int]) -> int:
#     return sum(numbers)
#
# a = [1, 2, 3, 4, 5]
# print(sum_numbers(a))

# from typing import Optional
#
# def find_user(user_id: int) -> Optional[str]:
#     if user_id == 1:
#         return "Пользователь найден"
#     return None
#
# find_user(2)

# from typing import Union
#
# def process_input(value: Union[int, str]):
#     return f"Ты передал: {value}"
#
# process_input('a')
# process_input(1)

# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def greet(self) -> str:
#         return f"Привет, меня зовут {self.name}!"
#
# user = User("Артем", 25)
# print(user.greet())

# def get_even_numbers(number: list[int]) -> list[int]:
#     my_list = []
#     for i in number:
#         if i % 2 == 0:
#             my_list.append(i)
#     return my_list
#
# a = [1, 2, 3, 4, 5]
# print(get_even_numbers(a))
