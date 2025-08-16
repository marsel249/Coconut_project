# # CinescopeFork\Modul_4\PydanticExamples\test_pydantic.py
# from typing import Optional
# from pydantic import BaseModel, Field
# from enum import Enum
# # from venv import logger
#
# import logging
# logger = logging.getLogger(__name__)
#
# class ProductType(str, Enum):
#     NEW = "new"
#     PREVIOUS_USE = "previous_use"
#
#
# class Manufacturer(BaseModel):
#     name: str
#     # city: Optional[str] = None
#     # street: Optional[str] = None
#     city: str | None = None
#     street: str | None = None
#
# class Product(BaseModel):
#     # поле name может иметь длину в диапазоне от 3 до 50 символов и является строкой
#     name: str = Field(..., min_length=3, max_length=50, description="Название продукта")
#     # Тоже самое, что и выше, по другому.. "..." - это дефолт значение
#     #name: str = Field(default=..., min_length=3, max_length=50)
#     # поле price должно быть больше 0
#     price: float = Field(..., gt=0, description="Цена продукта")
#     #есть параметры, например gt=0(>0), ge=0(>=0), lt=100(<100), le=100(<=100)
#     # поле in_stock принимает булево значение и установится по умолчанию = False
#     in_stock: bool = Field(default=False, description="Есть ли в наличии")
#     # поле color должно быть строкой и принимает значение "black" по умолчанию
#     color: str = "black"
#     # поле year не обязательное. можно не указывать при создании обьекта
#     year: Optional[int] = None
#     # поле product принимает тип Enum (может содержать только 1 из его значений)
#     product: ProductType
#     # поле manufacturer принимает тип другой BaseModel
#     manufacturer: Manufacturer
#
#
# def test_product():
#     # Пример создания обьекта + в поле price передаём строку вместо числа
#     product = Product(name="Laptop", price="999.99", product=ProductType.NEW, manufacturer=Manufacturer(name="MSI", city='Novosibirsk'))
#     logger.info(f"{product=}")
#     # Output: product=Product(name='Laptop', price=999.99, in_stock=False, color='black', year=None, product=<ProductType.NEW: 'new'>, manufacturer=Manufacturer(name='MSI', city='Novosibirsk', street=None))
#
#     # Пример конвертации обьекта в json
#     json_data = product.model_dump_json(exclude_unset=True)
#     logger.info(f"{json_data=}")
#     # Output: json_data='{"name":"Laptop","price":999.99,"product":"new","manufacturer":{"name":"MSI", "city":"Novosibirsk"}}'
#
#     # Пример конвертации json в обьект
#     new_product = Product.model_validate_json(json_data)
#     logger.info(f"{new_product=}")
#     # Output: new_product=Product(name='Laptop', price=999.99, in_stock=False, color='black', year=None, product=<ProductType.NEW: 'new'>, manufacturer=Manufacturer(name='MSI', city='Novosibirsk', street=None))




# from pydantic import BaseModel, Field
#
# class Product(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50, description="Название продукта")
#     price: float = Field(default="Unknown", gt=0, description="Цена продукта") # default="Unknown" - если не передавать занчение, будет - Unknown (необязательное)
#
# # # Попытка создать экземпляр без обязательных полей вызовет ошибку
# # try:
# #     product = Product()
# # except Exception as e:
# #     print(e)  # Output: "field required" для обоих полей
#
# # Корректное создание экземпляра
# product = Product(name="Laptop", price=1000.0)
#
# print(product)
#
# # Output: name='Laptop' price=1000.0

'''Field'''
# from pydantic import BaseModel, Field
# class Product(BaseModel):
#     name: str = Field(..., min_length=3)  # Обязательное поле
#     price: float = Field(default=0.0, ge=0)  # Необязательное поле с дефолтным значением

'''Optional и Default'''
# from typing import Optional
# from pydantic import BaseModel
#
# class Product(BaseModel):
#     name: str
#     year: Optional[int] = None  # Год выпуска не обязателен
#
# p1 = Product(name="Phone")
# p2 = Product(name="Phone", year=2022)

'''Enum'''
# from enum import Enum
# from pydantic import BaseModel
#
# class ProductType(str, Enum):
#     NEW = "new"
#     USED = "used"
#
# class Product(BaseModel):
#     name: str
#     product_type: ProductType
#
# product = Product(name='my name', product_type=ProductType.NEW)
# print(product)

'''Вложенные модели'''
# from pydantic import BaseModel
# from typing import Optional
#
# class Manufacturer(BaseModel):
#     name: str
#     city: Optional[str] = None
#
# class Product(BaseModel):
#     name: str
#     manufacturer: Manufacturer  # 👈 Вложенная модель
#
# my_object = Product(name='my_product', manufacturer=Manufacturer(name='name_my_Manufactor', city='Novosibirsk'))
# print(my_object)
#
# product = Product(name="Phone", manufacturer={"name": "Samsung"})
# print(product)
# # Product(name='Phone', manufacturer=Manufacturer(name='Samsung', city=None))

'''Конвертация в JSON'''

# from pydantic import BaseModel
#
# class Product(BaseModel):
#     name: str
#     price: float
#     random_inf : str | None = None
#
# product = Product(name="Laptop", price=999.99)
# json_data = product.model_dump_json(exclude_unset=True) # <- конвертация в json
# print(product) # name='Laptop' price=999.99 random_inf=None
# print(json_data) # '{"name": "Laptop", "price": 999.99}'
# json_data_new = product.model_dump_json # <- конвертация в json, без (exclude_unset=True)
# print(json_data_new) # <bound method BaseModel.model_dump_json of Product(name='Laptop', price=999.99, random_inf=None)>


'''Обратное преобразование (из JSON в объект)'''

# from pydantic import BaseModel
#
# class Product(BaseModel):
#     name: str
#     price: float
#     random_inf : str | None = None
#
# product = Product(name="Laptop", price=999.99)
# json_data = product.model_dump_json(exclude_unset=True)
# new_product = Product.model_validate_json(json_data)
# print(json_data) # {"name":"Laptop","price":999.99}
# print(new_product) # name='Laptop' price=999.99 random_inf=None

'''Автоматическая валидация данных'''

# from pydantic import BaseModel
#
# class Product(BaseModel):
#     name: str
#     price: float
#     random_inf : str | None = None
#
# try:
#     p = Product(name="TV", price="бесплатно") #Ошибка! "бесплатно" нельзя преобразовать в число.
# except Exception as e:
#     print(e)

# from pydantic import BaseModel, EmailStr, SecretStr, field_validator, model_validator, ConfigDict
#
# class Register(BaseModel):
#     model_config = ConfigDict(extra="forbid")
#
#     email: EmailStr
#     password: SecretStr
#     password_repeat: SecretStr
#
#     # 1) Нормализуем пароли (обрезаем пробелы) ДО типизации
#     @field_validator("password", "password_repeat", mode="before")
#     @classmethod
#     def strip_spaces(cls, v):
#         s = v.get_secret_value() if hasattr(v, "get_secret_value") else str(v)
#         return SecretStr(s.strip())
#
#     # 2) Проверяем силу пароля ПОСЛЕ типизации
#     @field_validator("password")
#     @classmethod
#     def strong_password(cls, v: SecretStr) -> SecretStr:
#         s = v.get_secret_value()
#         if len(s) < 8:
#             raise ValueError("min length = 8")
#         return v
#
#     # 3) До сборки модели можем переименовать ключи входа
#     @model_validator(mode="before")
#     @classmethod
#     def camel_to_snake(cls, data: dict):
#         if "passwordRepeat" in data and "password_repeat" not in data:
#             data = dict(data)
#             data["password_repeat"] = data.pop("passwordRepeat")
#         return data
#
#     # 4) После сборки модели сверяем поля между собой
#     @model_validator(mode="after")
#     def passwords_match(self):
#         if self.password.get_secret_value() != self.password_repeat.get_secret_value():
#             raise ValueError("Passwords don't match")
#         return self