from email.policy import default

import pytest
from module_5.Cinescope.utils.data_generator import DataGenerator
# from module_5.Cinescope.enums.enums import Roles
from pydantic import BaseModel
# from venv import logger
from enum import Enum
import logging
import random
from module_5.Cinescope.conftest import test_user, creation_user_data

logger = logging.getLogger(__name__)

@pytest.fixture
def registration_user_data():
    random_password = DataGenerator.generate_random_password()
    role_value = random.choice(list(Roles)).value #Можем выбирать рандомную роль

    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": [role_value], #[Roles.USER.value] - роль user, через class Enum, #Roles.USER.value - роль user, через импортированный файл Enum
        "banned": None,
        "verified": None
    }

class Roles(str, Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'
    SUPER_ADMIN = 'SUPER_ADMIN'

class UserPassword(BaseModel):
    email: str
    fullName: str
    password: str
    passwordRepeat: str
    roles: list
    banned: bool | None = False
    verified: bool | None = True

def test_verification_password(registration_user_data):
    user_password = UserPassword(**registration_user_data)
    assert user_password.email == registration_user_data.get('email')
    assert user_password.fullName == registration_user_data.get('fullName')
    assert user_password.password == registration_user_data.get('password')
    assert user_password.passwordRepeat == registration_user_data.get('passwordRepeat')
    assert user_password.roles == registration_user_data.get('roles')
    logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")

def test_verification_fixture_test_user(test_user):
    user_password = UserPassword(**test_user)
    user_password_data = user_password.model_dump_json(exclude_unset=True)
    print(user_password_data)
    assert user_password.email == test_user.get('email')
    assert user_password.fullName == test_user.get('fullName')
    assert user_password.password == test_user.get('password')
    assert user_password.passwordRepeat == test_user.get('passwordRepeat')
    assert user_password.roles == test_user.get('roles')
    logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")

def test_verification_fixture_creation_user_data(creation_user_data):
    user_password = UserPassword(**creation_user_data)
    user_password_data = user_password.model_dump_json()
    print(user_password_data)
    assert user_password.email == creation_user_data.get('email')
    assert user_password.fullName == creation_user_data.get('fullName')
    assert user_password.password == creation_user_data.get('password')
    assert user_password.passwordRepeat == creation_user_data.get('passwordRepeat')
    assert user_password.roles == creation_user_data.get('roles')
    logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")