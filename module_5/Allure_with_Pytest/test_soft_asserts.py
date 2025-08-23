# Modul_4\Cinescope\tests\api\test_auth.py

from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.conftest import TestUser, api_manager, session, test_user
from module_5.Cinescope.models.base_models import RegisterUserResponse
from module_5.Cinescope.enums.enums import Roles
import datetime
from pytest_check import check
import allure

@allure.title("Тест регистрации пользователя с помощью Mock")
@allure.severity(allure.severity_level.MINOR)
@allure.label("qa_name", "Ivan Petrovich")
def test_register_user_mock(api_manager: ApiManager, test_user: TestUser, mocker):
    with allure.step(" Мокаем метод register_user в auth_api"):
    # Ответ полученный из мок сервиса
        mock_response = RegisterUserResponse(  # Фиктивный ответ
            id="id",
            email="email@email.com",
            fullName="fullName",
            verified=True,
            banned=False,
            roles=[Roles.SUPER_ADMIN],
            createdAt=str(datetime.datetime.now())
        )

        mocker.patch.object(
            api_manager.auth_api,  # Объект, который нужно замокать
            'register_user',  # Метод, который нужно замокать
            return_value=mock_response  # Фиктивный ответ
        )
    with allure.step("Вызываем метод, который должен быть замокан"):
        register_user_response = api_manager.auth_api.register_user(test_user)

    with allure.step("Проверяем, что ответ соответствует ожидаемому"):
        with allure.step("Проверка поля персональных данных"):  # обратите внимание на вложенность allure.step
            with check:
                check.equal(register_user_response.fullName, "INCORRECT_NAME", "НЕСОВПАДЕНИЕ fullName")
                check.equal(register_user_response.email, mock_response.email, "Email не совпадает")

    with allure.step("Проверка поля banned"):
        with check("Проверка поля banned"):  # можно использовать вместо allure.step
            check.equal(register_user_response.banned, mock_response.banned)

    # Проверяем, что ответ соответствует ожидаемому

    with check:
        assert register_user_response.email == mock_response.email, "Email не совпадает"  # Проверка, такая же, как и проверка выше, дуль, для примера (положена в check, чтобы тест не останавливался)
        assert 1 + 3 == 2, "1 + 1 должно быть равно 2"
        assert 1 + 2 == 2, "1 + 1 должно быть равно 2"
        assert 1 + 1 == 2, "1 + 1 должно быть равно 2"
    print(f'\n Все проверки пройдены')
# Внутри мы можем проверять любое колличество ассертов но если хотябы 1 из них выстрелит
# тест продолжит свое выполнение

def test_check_functions():
    check.equal(1 + 1, 2, "Проверка сложения")
    check.not_equal(2 * 2, 5, "Проверка умножения")
    check.is_true(1 == 1, "Проверка истинности")
    check.is_in("hello", "hello world", "Проверка вхождения строки")

'''
- `check.equal(a, b, msg)`: Проверяет, что`a == b`.
- `check.not_equal(a, b, msg)`: Проверяет, что`a != b`.
- `check.is_true(x, msg)`: Проверяет, что`x`равно`True`.
- `check.is_false(x, msg)`: Проверяет, что`x`равно`False`.
- `check.is_none(x, msg)`: Проверяет, что 'x`равно`None`.
- `check.is_not_none(x, msg)`: Проверяет, что`x`не равно`None`.
- `check.is_in(a, b, msg)`: Проверяет, что`a`содержится в`b`.
- `check.is_not_in(a, b, msg)`: Проверяет, что`a`не содержится в`b`.
- `check.greater(a, b, msg)`: Проверяет, что`a > b`.
- `check.less(a, b, msg)`: Проверяет, что`a < b`.
- `check.greater_equal(a, b, msg)`: Проверяет, что`a >= b`.
- `check.less_equal(a, b, msg)`: Проверяет, что`a <= b`.
'''