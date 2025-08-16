
#
#
# # CinescopeFork\Modul_4\PydanticExamples\test_pydantic.py
# from pydantic import BaseModel, Field, field_validator, ValidationError
# from typing import Optional
# from venv import logger
#
# class PostgresClient:  # Mock - заглушка вместо реального сервиса. делающего запрос в базу данных
#     @staticmethod
#     def get(key: str):  # Всегда возвращает None
#         # return None
#         return key
#
# class Card(BaseModel):
#     pan: str = Field(..., min_length=16, max_length=16, description="Номер карты")
#     cvc: str = Field(...,  min_length=3, max_length=3)
#
#     @field_validator("pan")  # кастомный валидатор для проверки поля - pan
#     def check_pan(cls, value: str) -> str:
#         """
#             не самый лучший пример. Не стоит добавлять в валидаторы сложновесную логику,
#             но данным примером хочется показать что кастомные валидаторы лучше использовать
#             для ситуаций которые невозможно проверить доступной логикой Field
#         """
#         # Проверяем, существует ли карта в Redis
#         if PostgresClient.get(f'card_by_pan_{value}') is None:
#             raise ValueError("Такой карты не существует")
#         return value
# '''Проверяем, что номер карты содержит только цифры'''
#     @field_validator("pan", mode='before')
#     def check_pan_isdigit(cls, value: str) -> str:
#         if not value.isdigit():
#             raise ValueError("chars not is digit")
#         return value
#
# def test_field_validator():
# # Попытка создать объект с данными. Отсутствующими в базе данных
#     try:
#         card = Card(pan="1111222233334444", cvc="123")
#         logger.info(card)
#     except ValidationError as e:
#         logger.info(f"Ошибка валидации: {e}")
#         raise
#
# Card(pan="1234567890123456", cvc="999")  #  Всё ок
# Card(pan="1234abcd90123456", cvc="999")  #  Ошибка: PAN должен содержать только цифры

'''Как работают кастомные валидаторы в Pydantic?'''

# from pydantic import BaseModel, Field, field_validator
#
# class Card(BaseModel):
#     pan: str = Field(..., min_length=16, max_length=16, description="Номер карты")
#
#     @field_validator("pan")
#     def check_pan(cls, value: str) -> str:
#         """Проверяем, что PAN (номер карты) состоит только из цифр"""
#         if not value.isdigit():
#             raise ValueError("PAN должен содержать только цифры")
#         return value
#
# Card(pan="1234567890123456")  #  Всё ок
# Card(pan="1234abcd90123456")  #  Ошибка: PAN должен содержать только цифры

'''Использование внешних источников (например, базы данных)'''
# from pydantic import BaseModel, Field, field_validator
#
# class PostgresClient():
#     @staticmethod
#     def get(key: str):
#         # Заглушка: имитируем, что карт нет в базе
#         return None
#
# class Card(BaseModel):
#     pan: str = Field(..., min_length=16, max_length=16, description="Номер карты")
#     cvc: str = Field(..., min_length=3, max_length=3, description="CVC код")
#
#     @field_validator("pan")
#     def check_pan(cls, value: str) -> str:
#         """
#         Проверяем, есть ли карта в базе данных (здесь - в PostgresClient)
#         """
#         if PostgresClient.get(f'card_by_pan_{value}') is None:
#             raise ValueError("Такой карты не существует")
#         return value
#
# try:
#     card = Card(pan="1234567890123456", cvc="123")
# except ValueError as e:
#     print(e)  #  Такой карты не существует

'''Важно!!! Если Pydantic видит ошибку валидации, он даже не создаст объект!'''

'''Проверка нескольких полей одновременно

Если валидация должна зависеть от **нескольких полей**, используется `@model_validator`.

Пример: проверяем, что `cvc` у карты `Visa` должен быть именно 3 цифры, а у `Amex` – 4 цифры.'''

# from pydantic import BaseModel, Field, model_validator
# from enum import Enum
#
# class CardType(str, Enum):
#     VISA = "Visa"
#     AMEX = "American Express"
#
# class Card(BaseModel):
#     pan: str = Field(..., min_length=16, max_length=16)
#     cvc: str = Field(..., min_length=3, max_length=4)
#     card_type: CardType
#
#     @model_validator(mode="before")
#     def check_cvc_for_card_type(cls, values):
#         """
#         Проверяем, что:
#         - У карт VISA cvc == 3 цифры
#         - У карт AMEX cvc == 4 цифры
#         """
#         if values["card_type"] == CardType.VISA and len(values["cvc"]) != 3:
#             raise ValueError("CVC для VISA должен быть 3 цифры")
#         if values["card_type"] == CardType.AMEX and len(values["cvc"]) != 4:
#             raise ValueError("CVC для AMEX должен быть 4 цифры")
#         return values
#
# Card(pan="1234567890123456", cvc="123", card_type=CardType.VISA)  #  Всё ок
# Card(pan="1234567890123456", cvc="1234", card_type=CardType.VISA)  #  Ошибка: CVC для VISA должен быть 3 цифры
# Card(pan="1234567890123456", cvc="1234", card_type=CardType.AMEX)  #  Всё ок

'''
field_validator — работает с одним (или несколькими) полями по отдельности.
model_validator — работает с всем объектом целиком (может видеть/менять все поля сразу).

И у @field_validator, и у @model_validator по умолчанию mode="after".'''

'''Обработка ошибок валидации'''
# from pydantic import ValidationError
# from pydantic import BaseModel, Field
# from enum import Enum
#
# class CardType(str, Enum):
#     VISA = "Visa"
#     AMEX = "American Express"
#
# class Card(BaseModel):
#     pan: str = Field(..., min_length=16, max_length=16)
#     cvc: str = Field(..., min_length=3, max_length=4)
#     card_type: CardType
#
# try:
#     card = Card(pan="1234abcd90123456", cvc="12", card_type=CardType.VISA)
# except ValidationError as e:
#     print(e)

