from module_5.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.models.base_models import RegisterUserResponse, LoginResponse, TestUser, LoginRequest
from module_5.Cinescope.enums.enums import Roles
from module_5.Cinescope.db_requester.models import UserDBModel
from sqlalchemy.orm import Session


class TestAuthAPI:
    '''До рефакторинга
    def test_register_user(self, api_manager: ApiManager, test_user): # test_user - в последствии заменил на registration_user_data, чтобы не путаться
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"'''

    def test_register_user(self, api_manager: ApiManager, registration_user_data):
        response = api_manager.auth_api.register_user(user_data=registration_user_data)
        #assert response.status_code == 201, response.text (Так можно проверить статус код ответа, до того, как распарсили ответ)
        register_user_response = RegisterUserResponse(**response.json())
        assert register_user_response.email == registration_user_data.email, "Email не совпадает"
        assert "USER" in register_user_response.roles



    # def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
    #     """
    #     Тест на регистрацию и авторизацию пользователя.
    #     """
    #     login_data = {
    #         "email": registered_user["email"],
    #         "password": registered_user["password"]
    #     }
    #     response = api_manager.auth_api.login_user(login_data)
    #     response_data = response.json()
    #
    #     # Проверки
    #     assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
    #     assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user: TestUser):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = LoginResponse(**response.json())

        assert response_data.user.email == registered_user["email"], "Email не совпадает"




    # def test_authenticate(self, api_manager: ApiManager):
    #     """
    #     Тест на аутенфикацию админа
    #     """
    #
    #     response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)
    #
    #     # Проверки
    #     assert "roles" in response['user'], "Роли пользователя отсутствуют в ответе"
    #     assert "SUPER_ADMIN" in response['user']['roles'], "Роль SUPER_ADMIN должна быть у пользователя"

    def test_authenticate(self, api_manager: ApiManager):
        """
        Тест на аутенфикацию админа
        """
        email, password = SUPER_ADMIN_CREDS
        LoginRequest(email=email, password=password)
        response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)

        data = LoginResponse(**response)

        assert data.accessToken, "Токен доступа отсутствует"
        assert Roles.SUPER_ADMIN in data.user.roles, "Роль SUPER_ADMIN должна быть у пользователя"



        '''для негативных тестов
        resp = api_manager.auth_api.register_user(bad_user, expected_status=400)
        err = resp.json()
        assert err["statusCode"] == 400
        assert "password" in err["message"].lower()
        '''

        # Modul_4\Cinescope\tests\api\test_auth.py
    def test_register_user_db_session(self, api_manager: ApiManager, registration_user_data: TestUser, db_session_after_close: "Session"):
        """
        Тест на регистрацию пользователя с проверкой в базе данных.
        """
        # выполняем запрос на регистрацию нового пользователя
        response = api_manager.auth_api.register_user(registration_user_data)
        register_user_response = RegisterUserResponse(**response.json())

        # Проверяем добавил ли сервис Auth нового пользователя в базу данных
        users_from_db = db_session_after_close.query(UserDBModel).filter(UserDBModel.id == register_user_response.id)

        # получили обьект из бзы данных и проверили что он действительно существует в единственном экземпляре
        assert users_from_db.count() == 1, "обьект не попал в базу данных"
        # Достаем первый и единственный обьект из списка полученных
        user_from_db = users_from_db.first()
        # можем осуществить проверку всех полей в базе данных например Email
        assert user_from_db.email == registration_user_data.email, "Email не совпадает"