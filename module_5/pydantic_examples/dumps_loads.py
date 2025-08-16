'''- **Сериализация** – это преобразование объекта в строку или байтовый формат,
чтобы его можно было передавать по сети, сохранять в файл или базу данных
- **Десериализация** – это обратное преобразование строки или байтового формата обратно в объект
'''

'''Сериализация и десериализация с json'''
# import json
#
# # Объект Python (словарь)
# user = {
#     "name": "Alice",
#     "age": 25,
#     "email": "alice@example.com"
# }
#
# # Сериализация (Python → JSON)
# json_data = json.dumps(user)
# print(json_data)
# # Вывод: {"name": "Alice", "age": 25, "email": "alice@example.com"}
#
# # Десериализация (JSON → Python)
# user_obj = json.loads(json_data)
# print(user_obj["name"])  # Вывод: Alice

'''Сериализация и десериализация с pydantic'''
# from pydantic import BaseModel
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
# # Создаём объект
# user = User(name="Alice", age=25, email="alice@example.com")
#
# # Сериализация (Python → JSON)
# json_data = user.model_dump_json()
# print(json_data)
# # Вывод: {"name": "Alice", "age": 25, "email": "alice@example.com"}
#
# # Десериализация (JSON → Python)
# new_user = User.model_validate_json(json_data)
# print(new_user.name)  # Вывод: Alice


## Сериализация в файл
# from pydantic import BaseModel
# import json
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
# # Создаём объект
# user = User(name="Alice", age=25, email="alice@example.com")
#
# with open("user.json", "w") as file:
#     json.dump(user.model_dump(), file)
#
# # Десериализация из файла
# with open("user.json", "r") as file:
#     user_data = json.load(file)
#     new_user = User(**user_data)
#
# print(new_user)



# import pickle
#
# data = {"name": "Alice", "age": 25}
#
# # Сериализация
# binary_data = pickle.dumps(data)
#
# # Десериализация
# loaded_data = pickle.loads(binary_data)
# print(loaded_data)  # Вывод: {'name': 'Alice', 'age': 25}


