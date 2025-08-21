#
# from module_5.Cinescope.custom_requester.custom_requester import CustomRequester
# from module_5.Cinescope.constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT
# from module_5.Cinescope.constants import BASE_URL
# from module_5.Cinescope.models.base_models import TestUser
#
# class AuthAPI(CustomRequester):
#     """
#       Класс для работы с аутентификацией.
#       """
#
#     def __init__(self, session):
#         super().__init__(session=session, base_url=BASE_URL)
#
#    # def register_user(self, user_data, expected_status=201):
#    #      """
#    #      Регистрация нового пользователя.
#    #      :param user_data: Данные пользователя.
#    #      :param expected_status: Ожидаемый статус-код.
#    #      """
#    #      return self.send_request(
#    #          method="POST",
#    #          endpoint=REGISTER_ENDPOINT,
#    #          data=user_data,
#    #          expected_status=expected_status
#    #      )
#
#     # def register_user(self, user_data: TestUser):
#     #     """Регистрирует нового пользователя"""
#     #     payload = user_data.model_dump(mode="json", exclude_unset=True)  # сразу dict
#     #     return self.requester.send_request("POST", "/register", data=payload)
#
#     def register_user(self, user_data: TestUser, expected_status: int = 201):
#         """Регистрирует нового пользователя."""
#         payload = user_data.model_dump(mode="json", exclude_unset=True)
#         return self.send_request(
#             "POST",
#             "/register",
#             data=payload,
#             expected_status=expected_status,
#         )
#
#
#     def login_user(self, login_data, expected_status=200):
#         """
#         Авторизация пользователя.
#         :param login_data: Данные для логина.
#         :param expected_status: Ожидаемый статус-код.
#         """
#         return self.send_request(
#             method="POST",
#             endpoint=LOGIN_ENDPOINT,
#             data=login_data,
#             expected_status=expected_status
#         )
#
#     def authenticate(self, user_creds):
#         login_data = {
#             "email": user_creds[0],
#             "password": user_creds[1]
#         }
#
#         response = self.login_user(login_data)
#         response_data = response.json()
#         if "accessToken" not in response_data:
#             raise KeyError("token is missing")
#
#         token = response_data["accessToken"]
#         self._update_session_headers(**{"authorization": "Bearer " + token})
#
#         return response_data
#
#     def del_auth(self):
#
#         data = {"authorization": "Bearer "}
#
#         clear_token = self.session.headers.update(data)
#

# module_5/Cinescope/api/auth_api.py
from module_5.Cinescope.custom_requester.custom_requester import CustomRequester
from module_5.Cinescope.constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT, BASE_URL
from module_5.Cinescope.models.base_models import TestUser

class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def register_user(self, user_data: TestUser | dict, expected_status: int = 201):
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

    def authenticate(self, creds: tuple[str, str], expected_status: int = 200):
        body = {"email": creds[0], "password": creds[1]}
        resp = self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=body,
            expected_status=expected_status
        )
        data = resp.json()
        token = data.get("accessToken")
        if not token:
            raise KeyError("accessToken отсутствует в ответе")
        self._update_session_headers(authorization="Bearer " + token)
        return data

    def del_auth(self):
        self._update_session_headers(authorization="Bearer ")

    def update_session_headers_with_token(self, data):
        self._update_session_headers(authorization="Bearer " + data)