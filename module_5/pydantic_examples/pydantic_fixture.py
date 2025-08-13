import pytest
from module_5.Cinescope.utils.data_generator import DataGenerator
from module_5.Cinescope.enums.enums import Roles
from pydantic import BaseModel
from venv import logger

@pytest.fixture
def registration_user_data():
    random_password = DataGenerator.generate_random_password()

    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": Roles.USER.value #'USER'
    }

class UserPassword(BaseModel):
    email: str
    fullName: str
    password: str
    passwordRepeat: str
    roles: list

def test_verification_password(registration_user_data):
    user_password = UserPassword(**registration_user_data)
    assert user_password.email == registration_user_data.get('email')
    assert user_password.fullName == registration_user_data.get('fullName')
    assert user_password.password == registration_user_data.get('password')
    assert user_password.passwordRepeat == registration_user_data.get('passwordRepeat')
    assert user_password.roles == registration_user_data.get('roles')
    logger.info(f"{user_password.email=} {user_password.fullName=} {user_password.password=} {user_password.passwordRepeat=} {user_password.roles=}")

