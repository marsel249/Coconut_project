'''1. Что такое JSON Schema и зачем она нужна?'''

# # CinescopeFork\Modul_4\PydanticExamples\test_pydantic.py
# from pydantic import BaseModel
#
# class User2(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# def test_model_json_schema():
#     # Генерируем JSON Schema
#     user_schema = User2.model_json_schema()
#     # logger.info(user_schema)
#     #Output:
#     #{
#     #    'properties':
#     #    {
#     #        'id':{'title': 'Id', 'type': 'integer'},
#     #        'name':  {'title': 'Name', 'type': 'string'},
#     #        'email': {'title': 'Email', 'type': 'string'},
#     #        'is_active': {'default': True, 'title': 'Is Active', 'type': 'boolean'}
#     #    },
#     #    'required': ['id', 'name', 'email'],
#     #    'title': 'User2', 'type': 'object'
#     #}


# CinescopeFork\Modul_4\PydanticExamples\test_pydantic.py
# import jsonschema
# from pydantic import BaseModel
# import logging
# logger = logging.getLogger(__name__)
#
# class User2(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# # Данные для валидации
# user2_data = {
#     "id": 1,
#     "name": "Alice",
#     "email": "alice@example.com",
#     "is_active": True
# }
#
# user_schema = User2.model_json_schema()
#
# # Валидируем данные с использованием JSON Schema
# try:
#     jsonschema.validate(user2_data, user_schema)
#     logger.info("Данные валидны!")
# except jsonschema.ValidationError as e:
#     logger.info("Ошибка валидации:", e)
#
# def run():
#     logger.info("Данные валидны!")
#
# if __name__ == "__main__":
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s %(levelname)s %(name)s: %(message)s"
#     )
#     run()

'''Генерация JSON Schema из модели Pydantic'''

# from pydantic import BaseModel
# import jsonschema
# import logging
# logger = logging.getLogger(__name__)
#
# class User2(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# def test_model_json_schema():
#     # Генерируем JSON Schema
#     user_schema = User2.model_json_schema()
#     logger.info(user_schema)
#
# if __name__ == "__main__":
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s %(levelname)s %(name)s: %(message)s"
#     )
#     run()

#Output
# 13:09:12 INFO JSON_Schema: \
#     {'properties': {'id': {'title': 'Id', 'type': 'integer'},
#                     'name': {'title': 'Name', 'type': 'string'},
#                     'email': {'title': 'Email', 'type': 'string'},
#                     'is_active': {'default': True, 'title': 'Is Active', 'type': 'boolean'}},
#      'required': ['id', 'name', 'email'], 'title': 'User2', 'type': 'object'}

'''Использование JSON Schema в документации API'''

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class User2(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# @app.get("/users/")
# async def list_users():
#     return [{"id": 1, "name": "Ann"}]
#
# @app.post("/users/")
# async def create_user(user: User2):
#     return user

'''http://127.0.0.1:8000/docs
http://127.0.0.1:8000/users/ (чтоб работало, нужен app.get)

установить: pip3 install fastapi "uvicorn[standard]"
Запустить сервер(из папки с файлом с (app = FastAPI(), вместо 'main' - название файла)
python -m uvicorn main:app --reload
если порт 8000 занят,
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8001
'''


'''Валидация данных без использования Pydantic'''
# import jsonschema
# from pydantic import BaseModel
# import logging
# logger = logging.getLogger(__name__)
#
# if __name__ == "__main__":
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s %(levelname)s %(name)s: %(message)s"
#     )
#
# class User2(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# user2_data = {
#     "id": 1,
#     "name": "Alice",
#     "email": "alice@example.com",
#     "is_active": True
# }
#
# try:
#     jsonschema.validate(user2_data, User2.model_json_schema())
#     logger.info("✅ Данные валидны!")
# except jsonschema.ValidationError as e:
#     logger.info(f"❌ Ошибка валидации: {e}")





