# from email.policy import default
#
# import pytest
# from module_5.Cinescope.utils.data_generator import DataGenerator
# # from module_5.Cinescope.enums.enums import Roles
# from pydantic import BaseModel, field_validator, model_validator
# # from venv import logger
# from enum import Enum
# import logging
# import random
# from module_5.Cinescope.conftest import test_user, creation_user_data
#
# logger = logging.getLogger(__name__)
#
# @pytest.fixture
# def registration_user_data():
#     random_password = DataGenerator.generate_random_password()
#     role_value = random.choice(list(Roles)).value #Можем выбирать рандомную роль
#
#     return {
#         "email": DataGenerator.generate_random_email(),
#         "fullName": DataGenerator.generate_random_name(),
#         "password": random_password,
#         "passwordRepeat": random_password,
#         "roles": [role_value], #[Roles.USER.value] - роль user, через class Enum, #Roles.USER.value - роль user, через импортированный файл Enum
#         "banned": None,
#         "verified": None
#     }
#
# class Roles(str, Enum):
#     USER = 'USER'
#     ADMIN = 'ADMIN'
#     SUPER_ADMIN = 'SUPER_ADMIN'
#
# class UserPassword(BaseModel):
#     email: str
#     fullName: str
#     password: str
#     passwordRepeat: str
#     roles: list
#     banned: bool | None = False
#     verified: bool | None = True
#
#     @field_validator('email')
#     def check_special_digit_email(cls, value: str) -> str:
#         if '@' not in value:
#             raise ValueError('email need @')
#         return value
#
#     @model_validator(mode='after')
#     def check_password(self):
#         p1 = self.password
#         p2 = self.passwordRepeat
#         if p1 != p2:
#             raise ValueError('password dont match')
#         if len(self.password) < 8:
#             raise ValueError('password < 8 chars')
#         return self


# def test_verification_password(registration_user_data):
#     user_password = UserPassword(**registration_user_data)
#     assert user_password.email == registration_user_data.get('email')
#     assert user_password.fullName == registration_user_data.get('fullName')
#     assert user_password.password == registration_user_data.get('password')
#     assert user_password.passwordRepeat == registration_user_data.get('passwordRepeat')
#     assert user_password.roles == registration_user_data.get('roles')
#     logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")
#
# def test_verification_fixture_test_user(test_user):
#     user_password = UserPassword(**test_user)
#     user_password_data = user_password.model_dump_json(exclude_unset=True)
#     print(user_password_data)
#     assert user_password.email == test_user.get('email')
#     assert user_password.fullName == test_user.get('fullName')
#     assert user_password.password == test_user.get('password')
#     assert user_password.passwordRepeat == test_user.get('passwordRepeat')
#     assert user_password.roles == test_user.get('roles')
#     logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")
#
# def test_verification_fixture_creation_user_data(creation_user_data):
#     user_password = UserPassword(**creation_user_data)
#     user_password_data = user_password.model_dump_json()
#     print(user_password_data)
#     assert user_password.email == creation_user_data.get('email')
#     assert user_password.fullName == creation_user_data.get('fullName')
#     assert user_password.password == creation_user_data.get('password')
#     assert user_password.passwordRepeat == creation_user_data.get('passwordRepeat')
#     assert user_password.roles == creation_user_data.get('roles')
#     logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")

# from pydantic import ValidationError
#
# def demo_run():
#     ok_pwd = "Abcdef12"         # длина ≥ 8
#     short_pwd = "Abc12"         # короткий
#     email_ok = "user@example.com"
#     email_bad = "user.example.com"  # без @
#
#     cases = [
#         ("ok", {
#             "email": email_ok,
#             "fullName": "John Smith",
#             "password": ok_pwd,
#             "passwordRepeat": ok_pwd,
#             "roles": ["USER"],
#             "banned": False,
#             "verified": True,
#         }),
#         ("bad_email_no_at", {
#             "email": email_bad,           # <- нет "@"
#             "fullName": "Jane",
#             "password": ok_pwd,
#             "passwordRepeat": ok_pwd,
#             "roles": ["USER"],
#             "banned": False,
#             "verified": True,
#         }),
#         ("passwords_mismatch", {
#             "email": email_ok,
#             "fullName": "Jane",
#             "password": ok_pwd,
#             "passwordRepeat": ok_pwd + "X",  # <- не совпадает
#             "roles": ["ADMIN"],
#             "banned": None,
#             "verified": None,
#         }),
#         ("password_too_short", {
#             "email": email_ok,
#             "fullName": "Bob",
#             "password": short_pwd,        # <- короткий
#             "passwordRepeat": short_pwd,
#             "roles": ["SUPER_ADMIN"],
#             "banned": False,
#             "verified": True,
#         }),
#         ("roles_wrong_type", {
#             "email": email_ok,
#             "fullName": "Ann",
#             "password": ok_pwd,
#             "passwordRepeat": ok_pwd,
#             "roles": "USER",              # <- строка вместо списка
#             "banned": False,
#             "verified": True,
#         }),
#     ]
#
#     for name, data in cases:
#         print(f"\n=== CASE: {name} ===")
#         try:
#             obj = UserPassword(**data)
#             print("OK ->", obj.model_dump(exclude_unset=True))
#         except ValidationError as e:
#             # Собранные ошибки валидации
#             print("ERROR ->", e.errors())
#         except Exception as e:
#             # На случай неожиданных ValueError из валидаторов
#             print("ERROR (raw) ->", type(e).__name__, str(e))
#
# if __name__ == "__main__":
#     import logging
#     logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
#     demo_run()



# from module_5.pydantic_examples.api_requests import product


from pydantic import BaseModel, ConfigDict
from enum import Enum

class ProductType(str, Enum):
    CAR = 'Car'
    FLY = 'Fly'

class Product(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    price: float
    in_stock: bool = True
    Product_type: ProductType

product = Product(name='MyName', price=20, Product_type=ProductType.CAR)

json_data = product.model_dump_json()
print(json_data)

loaded_data = Product.model_validate_json(json_data)
print(loaded_data.name)