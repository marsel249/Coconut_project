'''авторизация'''
# import requests
# from requests.auth import HTTPBasicAuth
#
# url = "https://httpbin.org/basic-auth/user/passwd"  # URL, требующий Basic Auth
#
# response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))
#
# print(f"Status code: {response.status_code}")
# print(response.json())

'''не корретные данные'''
# import requests
# from requests.auth import HTTPBasicAuth
#
# url = "https://httpbin.org/basic-auth/user/passwd"
#
# response_wrong = requests.get(url, auth=HTTPBasicAuth('wrong_user', 'wrong_passwd'))
#
# print(f"Status code (wrong credentials): {response_wrong.status_code}") # Статус код будет 401 (Unauthorized)
# print(response_wrong.text) # Тело ответа будет содержать сообщение об ошибке

'''Bearer Token'''
# import requests
#
# url = "https://httpbin.org/bearer"
# token = "my_secret_token"
# headers = {'Authorization': f'Bearer {token}'}
#
# response = requests.get(url, headers=headers)
#
# print(f"Status code: {response.status_code}")
# print(response.json())

'''API Key'''
# #Пример с апи ключом в заголовке
# import requests
#
# url = "https://httpbin.org/headers"
# api_key = "my_api_key"
# headers = {'X-API-Key': api_key}
#
# response = requests.get(url, headers=headers)
#
# print(f"Status code: {response.status_code}")
# print(response.json()) # В json будет информация о переданных заголовках, включая X-API-Key

# #Пример с апи ключом в параметрах запроса
# import requests
#
# url = "https://httpbin.org/get"
# api_key = "my_api_key"
# params = {'api_key': api_key}
#
# response = requests.get(url, params=params)
#
# print(f"Status code: {response.status_code}")
# print(response.json()) # В json будет информация о переданных параметрах, включая api_key

'''refresh token'''

# import requests
#
# REFRESH_TOKEN_URL = "https://example.com/api/token/refresh"
#
# refresh_token = "YOUR_REFRESH_TOKEN"
#
# def refresh_access_token(refresh_token):
#     """Обновляет access токен с помощью refresh токена."""
#     data = {"refresh_token": refresh_token}
#     response = requests.post(REFRESH_TOKEN_URL, json=data)
#
#     if response.status_code == 200:
#         new_access_token = response.json().get("access_token")
#         new_refresh_token = response.json().get("refresh_token")
#         return new_access_token, new_refresh_token
#     else:
#         print(f"Ошибка обновления токена: {response.status_code}")
#         return None, None
#
# # Получаем оба токена
# new_access_token, new_refresh_token = refresh_access_token(refresh_token) #На выходе функции мы получаем кортеж..
# #С помошью перечисления параметров, мы распаковываем кортеж в две переменных, примерно как при: "for A, B in variable:.."
#
# if new_access_token:
#     print(f"Новый access токен: {new_access_token}")
#     if new_refresh_token:
#         print(f"Новый refresh токен: {new_refresh_token}")
#
#     # Дальше суем в заголовок/куки - в зависимости от реализации
#     headers = {"Authorization": f"Bearer {new_access_token}"}
#     response = requests.get("https://example.com/api/protected", headers=headers)
#     # ...

'''OAuth2'''

# import requests
#
# # Готовим данные
# auth_url = 'https://api.example.com/oauth2/token'
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'
#
# data = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret
# }
#
# # Получаем токен
# token_response = requests.post(auth_url, data=data)
# access_token = token_response.json().get('access_token')
#
# # используем
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
#
# response = requests.get('https://api.example.com/secure-data', headers=headers)
#
# if response.status_code == 200:
#     print("Авторизация через OAuth2 успешна!")
#     print(response.json())