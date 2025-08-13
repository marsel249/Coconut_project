from pydantic import BaseModel
from venv import logger


class User(BaseModel):  # Создается класс User с помощью BaseModel от pydantic и указывается
    name: str       # что имя должно быть строкой
    age: int        # возраст должен быть числом
    adult: bool     # поле совершеннолетие должно быть булевым значением


def get_user():  # функция get_user возвращает объект dict с следующими полями
    return {
        "name": "Alice",
        "age": '25',
        "adult": "true"
    }


def test_user_data():
    user = User(**get_user())  # Проверяем возможность конвертации данных и соответствия типов данных с помощью Pydantic
    #User(name="Alice", age=25, adult="true"), распаковываем словарь
    assert user.name == "Alice"  # Возможность дополнительных проверок
    logger.info(f"{user.name=} {user.age=} {user.adult=}")  # а также возможность удобного взаимодействия
    # вывод - user.name='Alice' user.age=25 user.adult=True
