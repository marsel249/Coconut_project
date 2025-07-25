#booker

'''ДО рефакторинга'''

# import requests
# from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT
# from faker import Faker
#
# faker = Faker()
#
# class TestAuthAPI:
#     def test_register_user(self, test_user):
#         # URL для регистрации
#         register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
#
#         # Отправка запроса на регистрацию
#         response = requests.post(register_url, json=test_user, headers=HEADERS)
#
#         # Логируем ответ для диагностики
#         print(f"Response status: {response.status_code}")
#         print(f"Response body: {response.text}")
#
#         # Проверки
#         assert response.status_code == 201, "Ошибка регистрации пользователя"
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#
#         # Проверяем, что роль USER назначена по умолчанию
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
# #Проверка на успешную аутенфикацию (PASS)
#     def test_auth_user(self, test_user):
#         #Registration
#         register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
#         response = requests.post(register_url, json=test_user, headers=HEADERS)
#
#         assert response.status_code == 201, "Ошибка регистрации пользователя"
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
#         #Login
#         login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'
#         login_data = {
#             'email' : test_user['email'],
#             'password' : test_user['password']
#         }
#         response = requests.post(f'{BASE_URL}{LOGIN_ENDPOINT}', json=login_data, headers=HEADERS)
#         assert response.status_code == 200, "Ошибка аутенфикации пользователя"
#         assert 'accessToken' in response.json(), 'в ответе отсутствует токен'
#         assert login_data['email'] == response.json()['user']['email'], 'email при регистрации отличается от текущего'
#         token = response.json()['accessToken']
#         r_token = response.json()['refreshToken'] #Не нашел в доке, как передается рефреш токен,
#         # при запросе(когда нужно обновить токен), в боди, или в хедерах в сессии.
#         s = requests.session()
#         s.headers.update(HEADERS)
#         s.headers.update({"Authorization": f"Bearer {token}"})
#
# #Проверка на логин с рандомным паролем (PASS)
#     def test_negative_auth_user1(self, test_user):
#         #Registration
#         register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
#         response = requests.post(register_url, json=test_user, headers=HEADERS)
#
#         assert response.status_code == 201, "Ошибка регистрации пользователя"
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
#         #Login
#         login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'
#         login_data = {
#             'email' : test_user['email'],
#             'password' : faker.password(length=8)
#         }
#         response = requests.post(f'{BASE_URL}{LOGIN_ENDPOINT}', json=login_data, headers=HEADERS)
#         assert response.status_code == 401, "успешная аутенфикация пользователя, при не верном пароле"
#         assert 'Неверный логин или пароль' in response.json()['message']
#
# #Проверка на логин с рандомным email (PASS)
#     def test_negative_auth_user2(self, test_user):
#         #Registration
#         register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
#         response = requests.post(register_url, json=test_user, headers=HEADERS)
#
#         assert response.status_code == 201, "Ошибка регистрации пользователя"
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
#         #Login
#         login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'
#         login_data = {
#             'email' : faker.email(),
#             'password' : test_user['password']
#         }
#         response = requests.post(login_url, json=login_data, headers=HEADERS)
#         assert response.status_code == 401, "успешная аутенфикация пользователя, при не верном email"
#         assert 'Неверный логин или пароль' in response.json()['message']
#
# #Проверка на логин с пустым телом запроса (PASS)
#     def test_negative_auth_user2(self, test_user):
#         #Registration
#         register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
#         response = requests.post(register_url, json=test_user, headers=HEADERS)
#
#         assert response.status_code == 201, "Ошибка регистрации пользователя"
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
#         #Login
#         login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'
#         login_data = {}
#         response = requests.post(f'{BASE_URL}{LOGIN_ENDPOINT}', json=login_data, headers=HEADERS)
#         assert response.status_code == 401, "успешная аутенфикация пользователя, при пустом login_data"
#         assert 'Неверный логин или пароль' in response.json()['message']

'''ПОСЛЕ рефакторинга'''


# import pytest
# from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT
#
#
# class TestAuthAPI:
#     def test_register_user(self, requester, test_user):
#         """
#         Тест на регистрацию пользователя.
#         """
#         response = requester.send_request(
#             method="POST",
#             endpoint=REGISTER_ENDPOINT,
#             data=test_user,
#             expected_status=201
#         )
#         response_data = response.json()
#         assert response_data["email"] == test_user["email"], "Email не совпадает"
#         assert "id" in response_data, "ID пользователя отсутствует в ответе"
#         assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
#         assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"
#
#     def test_register_and_login_user(self, requester, registered_user):
#         """
#         Тест на регистрацию и авторизацию пользователя.
#         """
#         login_data = {
#             "email": registered_user["email"],
#             "password": registered_user["password"]
#         }
#         response = requester.send_request(
#             method="POST",
#             endpoint=LOGIN_ENDPOINT,
#             data=login_data,
#             expected_status=200
#         )
#         response_data = response.json()
#         assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
#         assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"

'''Мы пережили еще один рефакторинг..'''

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager

class TestAuthAPI:
    def test_register_user(self, api_manager: ApiManager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"
