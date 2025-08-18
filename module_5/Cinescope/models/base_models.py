import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict
from module_5.Cinescope.enums.enums import Roles

class TestUser(BaseModel):

    email: str
    fullName: str
    password: str
    passwordRepeat: str = Field(..., min_length=1, max_length=20, description="passwordRepeat должен вполностью совпадать с полем password")
    roles: list[Roles] = Field(default_factory=lambda: [Roles.USER])#[Roles.USER]
    verified: Optional[bool] = None
    banned: Optional[bool] = None

    model_config = ConfigDict(use_enum_values=True)  # Enum -> .value

    @field_validator("passwordRepeat")
    def check_password_repeat(cls, value: str, info: ValidationInfo) -> str:
        # Проверяем, совпадение паролей
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Пароли не совпадают")
        return value

    # # Добавляем кастомный JSON-сериализатор для Enum
    # class Config:
    #     json_encoders = {
    #         Roles: lambda v: v.value  # Преобразуем Enum в строку
    #     }

class RegisterUserResponse(BaseModel):
    id: str
    email: str = Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", description="Email пользователя")
    fullName: str = Field(min_length=1, max_length=100, description="Полное имя пользователя")
    verified: bool
    banned: bool
    roles: List[Roles]
    createdAt: str = Field(description="Дата и время создания пользователя в формате ISO 8601")

    @field_validator("createdAt")
    def validate_created_at(cls, value: str) -> str:
        # Валидатор для проверки формата даты и времени (ISO 8601).
        try:
            datetime.datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("Некорректный формат даты и времени. Ожидается формат ISO 8601.")
        return value


'''
class User(BaseModel):
    role: Roles

    class Config:
        json_encoders = {Roles: lambda v: v.value}

u = User(role=Roles.ADMIN)
u.model_dump()        # {'role': <Roles.ADMIN: 'ADMIN'>}
u.model_dump_json()   # '{"role":"ADMIN"}'
'''

'''
from pydantic import BaseModel, field_serializer

class User(BaseModel):
    roles: list[Roles]

    @field_serializer('roles')
    def ser_roles(self, roles: list[Roles]):
        return [r.value for r in roles]
'''

'''
Lambda

# Отсортировать строки по длине
names = ["Ann", "Elizabeth", "Bob"]
sorted_names = sorted(names, key=lambda s: len(s))  # ['Ann', 'Bob', 'Elizabeth']

# Оставить только чётные числа
evens = list(filter(lambda x: x % 2 == 0, range(6)))  # [0, 2, 4]

# Pydantic (v1-стиль): сериализовать Enum по value
class Config:
    json_encoders = {Roles: lambda v: v.value}
    
    
Любую lambda можно переписать как обычную функцию:

def enum_to_value(v):
    return v.value

class Config:
    json_encoders = {Roles: enum_to_value}

'''