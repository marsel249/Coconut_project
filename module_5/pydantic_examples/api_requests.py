#Псевдокод. Рельную работоспособность FastApi рассмотрим в следующих уроках
from itertools import product

# from fastapi import APIRouter, FastAPI
# from pydantic import BaseModel, Field
# import requests
#
# class RegisterRequest(BaseModel):
# 	login: str  = Field(..., min_length=6, max_length=10)
# 	password: str  = Field(..., min_length=6, max_length=10)
#
# mock_server_router = APIRouter()
#
# @mock_server_router.post("/register")
# async def register(register_request: RegisterRequest):
# 	register_request.login
# 	register_request.password
#
# app = FastAPI()
# app.include_router(mock_server_router)
#
# #Псевдокод так как отсутствует сервер с ендпойнтом api.example.com/product
# # CinescopeFork\Modul_4\PydanticExamples\test_pydantic.py
# product_id = 1
# response = requests.get(f"https://api.example.com/product/{product_id}")
# response.json()
#  #{"name": "Laptop", "price": 999.99, "in_stock": "false", "product": "new",  "color": "black", "manufacturer": {"name": "MSI"}}




# from fastapi import FastAPI, APIRouter
# from pydantic import BaseModel, Field
#
# app = FastAPI()
# router = APIRouter()
#
# # Модель запроса с валидацией
# class RegisterRequest(BaseModel):
#     login: str = Field(..., min_length=6, max_length=10)
#     password: str = Field(..., min_length=6, max_length=10)
#
# # Эндпоинт регистрации
# @router.post("/register")
# async def register(register_request: RegisterRequest):
#     return {"message": "Пользователь зарегистрирован!", "data": register_request}
#
# app.include_router(router)

'''Валидация ответа API'''

# import requests
# from pydantic import BaseModel
#
# # Модель ответа API
# class Product(BaseModel):
#     name: str
#     price: float
#     in_stock: bool
#     product: str
#     color: str
#     manufacturer: dict
#
# # Делаем запрос
# response = requests.get("https://api.example.com/product/123")
#
# # Получаем JSON-ответ
# product_json = response.json()
#
# # Валидация через Pydantic
# try:
#     product = Product(**product_json)
#     print("✅ Данные валидны:", product)
# except Exception as e:
#     print("❌ Ошибка валидации:", e)




from pydantic import field_validator, BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
    product: str
    color: str
    manufacturer: dict

    # Кастомный валидатор для `in_stock`
    @field_validator("in_stock", mode="before")
    def convert_boolean(cls, value):
        if isinstance(value, str):
            return value.lower() == "true"
        return value

product_json = {
    "name": "Laptop",
    "price": 999.99,
    "in_stock": "false",  # ✅ Автоматически преобразуется в False
    "product": "new",
    "color": "black",
    "manufacturer": {"name": "MSI"}
}

product = Product(**product_json)
print(product.in_stock)  # 🔹 False

