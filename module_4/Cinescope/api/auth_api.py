
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT
from module_4.Cinescope.constants import BASE_URL

class AuthAPI(CustomRequester):
    """
      Класс для работы с аутентификацией.
      """

    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def register_user(self, user_data, expected_status=201):
        """
        Регистрация нового пользователя.
        :param user_data: Данные пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=expected_status
        )

    def login_user(self, login_data, expected_status=200):
        """
        Авторизация пользователя.
        :param login_data: Данные для логина.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=expected_status
        )

    def authenticate(self, user_creds):
        login_data = {
            "email": user_creds[0],
            "password": user_creds[1]
        }

        response = self.login_user(login_data)
        response_data = response.json()
        if "accessToken" not in response_data:
            raise KeyError("token is missing")

        token = response_data["accessToken"]
        self._update_session_headers(**{"authorization": "Bearer " + token})

        return response_data

    def del_auth(self):

        data = {"authorization": "Bearer "}

        clear_token = self.session.headers.update(data)