# import pytest
# from module_5.Cinescope.utils.data_generator import DataGenerator
# from module_5.Cinescope.enums.enums import Roles
# from pydantic import BaseModel
# from venv import logger
#
# @pytest.fixture
# def registration_user_data():
#     random_password = DataGenerator.generate_random_password()
#
#     return {
#         "email": DataGenerator.generate_random_email(),
#         "fullName": DataGenerator.generate_random_name(),
#         "password": random_password,
#         "passwordRepeat": random_password,
#         "roles": Roles.USER.value #'USER'
#     }
#
# class UserPassword(BaseModel):
#     email: str
#     fullName: str
#     password: str
#     passwordRepeat: str
#     roles: list
#
# def test_verification_password(registration_user_data):
#     user_password = UserPassword(**registration_user_data)
#     assert user_password.email == registration_user_data.get('email')
#     assert user_password.fullName == registration_user_data.get('fullName')
#     assert user_password.password == registration_user_data.get('password')
#     assert user_password.passwordRepeat == registration_user_data.get('passwordRepeat')
#     assert user_password.roles == registration_user_data.get('roles')
#     logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")




# from pydantic import BaseModel, EmailStr, Field, model_validator, ConfigDict, SecretStr
#
# class Register(BaseModel):
#     model_config = ConfigDict(extra="forbid")
#     email: EmailStr
#     password: SecretStr = Field(min_length=8, max_length=16)
#     password_repeat: SecretStr = Field(min_length=8, max_length=16) #Использование секрет строки, для маскировки пароля
#
#     @model_validator(mode='after')
#     def check_match(self):
#         if self.password != self.password_repeat:
#             raise ValueError('Password dont match')
#         return self
#
# r = Register.model_validate({'email': 'abc@mail.com',
#                              'password':'12345678',
#                              'password_repeat':'12345678'})
# print(r.model_dump())


#Другой вариант проверки длины пароля, пароль скрыт
# from pydantic import BaseModel, EmailStr, field_validator, model_validator, ConfigDict, SecretStr
#
# class Register(BaseModel):
#     model_config = ConfigDict(extra="forbid")
#
#     email: EmailStr
#     password: SecretStr
#     password_repeat: SecretStr
#
#     @field_validator('password', 'password_repeat')
#     @classmethod
#     def check_len(cls, i: SecretStr) -> SecretStr:
#         x = i.get_secret_value()
#         if not (8 <= len(x) <= 16):
#             raise ValueError('password must be 8-16 chars')
#         return i
#
#     @model_validator(mode='after')
#     def check_match(self):
#         p1 = self.password.get_secret_value()
#         p2 = self.password_repeat.get_secret_value()
#         if p1 != p2:
#             raise ValueError('Password dont match')
#         return self
#
# r = Register.model_validate({'email': 'abc@mail.com',
#                              'password':'12345678',
#                              'password_repeat':'12345678'})
# print(r)
# print(r.model_dump())
# print(r.model_dump(exclude={"password", "password_repeat"}))


# + одна цифра, одна буква
# from pydantic import BaseModel, EmailStr, SecretStr, field_validator, model_validator, ConfigDict
#
# class Register(BaseModel):
#     model_config = ConfigDict(extra="forbid")
#
#     email: EmailStr
#     password: SecretStr
#     password_repeat: SecretStr
#
#     # 1) Нормализуем ввод: обрезаем пробелы по краям (mode="before")
#     @field_validator("password", "password_repeat", mode="before")
#     @classmethod
#     def strip_spaces(cls, v):
#         s = v.get_secret_value() if isinstance(v, SecretStr) else str(v)
#         return SecretStr(s.strip())
#
#     # 2) Правила силы пароля
#     @field_validator("password", "password_repeat")
#     @classmethod
#     def strong_enough(cls, v: SecretStr) -> SecretStr:
#         s = v.get_secret_value()
#         if not (8 <= len(s) <= 16):
#             raise ValueError("Password must be 8..16 chars")
#         if " " in s:
#             raise ValueError("Password must not contain spaces")
#         if not any(ch.isdigit() for ch in s):
#             raise ValueError("Password must contain at least one digit")
#         if not any(ch.isalpha() for ch in s):
#             raise ValueError("Password must contain at least one letter")
#         # Если нужно требовать спецсимвол, раскомментируй:
#         # if not any(not ch.isalnum() for ch in s):
#         #     raise ValueError("Password must contain a special character")
#         return v
#
#     # 3) Совпадение паролей
#     @model_validator(mode="after")
#     def check_match(self):
#         if self.password.get_secret_value() != self.password_repeat.get_secret_value():
#             raise ValueError("Passwords don't match")
#         return self
#
# # пример
# r = Register.model_validate({
#     "email": "abc@mail.com",
#     "password": "  Abc12345  ",
#     "password_repeat": "Abc12345"
# })
#
# print(r)  # пароли маскированы
# # Если выводишь наружу, исключи пароли:
# print(r.model_dump(exclude={"password", "password_repeat"}))
# # Когда нужно отправить в хешер:
# plain = r.password.get_secret_value()

#минимум 1 цифра, 1 буква, 1 заглавная, 1 строчная, 1 спецсимвол, без пробелов, длина 8–16.

# from pydantic import BaseModel, EmailStr, SecretStr, field_validator, model_validator, ConfigDict
#
# class Register(BaseModel):
#     model_config = ConfigDict(extra="forbid")
#
#     email: EmailStr
#     password: SecretStr
#     password_repeat: SecretStr
#
#     # 1) нормализуем ввод (обрезка пробелов по краям)
#     @field_validator("password", "password_repeat", mode="before")
#     @classmethod
#     def strip_spaces(cls, v):
#         s = v.get_secret_value() if isinstance(v, SecretStr) else str(v)
#         return SecretStr(s.strip())
#
#     # 2) проверки силы пароля
#     @field_validator("password", "password_repeat")
#     @classmethod
#     def strong_enough(cls, v: SecretStr) -> SecretStr:
#         s = v.get_secret_value()
#         if not (8 <= len(s) <= 16):
#             raise ValueError("Password must be 8..16 chars")
#         if " " in s:
#             raise ValueError("Password must not contain spaces")
#         if not any(ch.isdigit() for ch in s):
#             raise ValueError("Password must contain at least one digit")
#         if not any(ch.isalpha() for ch in s):
#             raise ValueError("Password must contain at least one letter")
#         if not any(ch.isupper() for ch in s):
#             raise ValueError("Password must contain at least one uppercase letter")
#         if not any(ch.islower() for ch in s):
#             raise ValueError("Password must contain at least one lowercase letter")
#         if not any(not ch.isalnum() for ch in s):
#             raise ValueError("Password must contain at least one special character")
#         return v
#
#     # 3) совпадение паролей
#     @model_validator(mode="after")
#     def check_match(self):
#         if self.password.get_secret_value() != self.password_repeat.get_secret_value():
#             raise ValueError("Passwords don't match")
#         return self
#
# # пример использования:
# r = Register.model_validate({
#     "email": "abc@mail.com",
#     "password": "Abc12345!",
#     "password_repeat": "Abc12345!"
# })
# print(r.model_dump(exclude={"password", "password_repeat"}))

from pydantic import BaseModel, field_validator, ConfigDict, ValidationError
from typing import List

class RolesModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    roles: List[str]

    @field_validator("roles", mode="before")
    @classmethod
    def normalize_roles(cls, v):
        # Принять и строку "USER, admin", и список ["USER", " admin "]
        if isinstance(v, str):
            # parts = [p.strip() for p in v.split(",")]

            parts = []
            for p in v.split(","):
                p = p.strip()
                parts.append(p)

        elif isinstance(v, (list, tuple, set)):
            # parts = [str(p).strip() for p in v]

            parts = []
            for p in v:
                p = str(p).strip()
                parts.append(p)
        else:
            raise TypeError("roles must be list[str] or comma-separated string")

        # Удаляем пустые, нормализуем регистр
        # parts = [p.upper() for p in parts if p]

        tmp = []
        for p in parts:
            if p:
                tmp.append(p.upper())
        parts = tmp

        # Дедупликация с сохранением порядка
        # seen, out = set(), []

        seen = set()
        out = []
        for p in parts:
            if p not in seen:
                seen.add(p)
                out.append(p)
        return out

        # out = []
        # for p in parts:
        #     if p not in out:
        #         out.append(p)
        # return out
        # Работает, но медленнее, чем вариант выше

    @field_validator("roles")
    @classmethod
    def check_allowed(cls, roles: List[str]) -> List[str]:
        allowed = {"USER", "ADMIN", "SUPER_ADMIN"}
        bad = [r for r in roles if r not in allowed]
        if bad:
            raise ValueError(f"Unknown roles: {bad}. Allowed: {sorted(allowed)}")
        return roles

a = RolesModel(roles="USER, admin , , user")      # -> roles=['USER', 'ADMIN']
b = RolesModel(roles=[" Admin ", "SUPER_ADMIN"])  # -> roles=['ADMIN', 'SUPER_ADMIN']
# c = RolesModel(roles="guest")                     # -> ValidationError (Unknown roles)
print(a)
print(b)
# print(c)

try:
    RolesModel(roles="guest")
except ValidationError as e:
    print(e.errors())  # список dict’ов с loc/msg/type






