'''Делаем GET запрос, с помощью библиотеки реквест, используем методы, статус код, и текст, для просмотра ответа'''

import requests  # Импортируем библиотеку

# response = requests.get('https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown')
# print(response.status_code)
# print(response.text)

# # Делаем GET запрос к API
# response = requests.get('https://restful-booker.herokuapp.com/booking')
#
# # Смотрим, что нам пришло
# print(f"Статус ответа: {response.status_code}")
# print(f"Тело ответа: {response.text}")

'''используя *.json() - ответ из json - преобразуется в словарь'''

# import requests
#
# response = requests.get('https://restful-booker.herokuapp.com/booking')
#
# data = response.json()
#
# # Тело ответа в словаре
# print(f"Тело ответа: {data}")
# print(f"можно обратиться по ключу, например к первому элементу: {data[0]}")

'''Подстановка переменной в качестве параметра'''

# import requests
#
# booking_id = 1
# response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
#
# data = response.json()
#
# # Тело ответа в словаре
# print(f"Тело ответа: {data}")

'''Подстановка переменных, в качестве параметров, через params'''

# import requests
# """
# response = requests.get(f'https://restful-booker.herokuapp.com/booking?firstname=Sally')
# """
# response = requests.get(f'https://restful-booker.herokuapp.com/booking',
#                         params={'firstname': 'Sally'})
#
# data = response.json()
#
# # Тело ответа в словаре
# print(f"Тело ответа: {data}")

'''Работа с заголовками, с помощью headers'''

# import requests
#
# # Создаём словарь с заголовками
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
#     'Accept': 'application/json'
# }
#
# # Передаём заголовки в запрос
# response = requests.get(
#     'https://restful-booker.herokuapp.com/booking',
#     headers=headers
# )

'''try, except'''

# try:
# # Делаем запрос
#     response = requests.get('https://restful-booker.herokuapp.com/booking')
# #     response = requests.get('https://restful-booker.herokuapp.com/booking1notwork')
#
# # Проверяем статус ответа
#     response.raise_for_status()  # Вызовет исключение, если статус не 2XX
#
# # Если всё хорошо, работаем с данными
#     data = response.json()
#     print(f"Получены данные: {data}")
#
# except requests.exceptions.ConnectionError:
#     print("Не удалось подключиться к серверу")
# # Тут можно, например, повторить запрос позже
#
# except requests.exceptions.Timeout:
#     print("Сервер не отвечает слишком долго")
# # Тут можно увеличить время ожидания и повторить
#
# except requests.exceptions.HTTPError as http_err:
#     print(f"Произошла HTTP ошибка: {http_err}")
# # Например, можно проверить статус код и принять решение, что делать
#
# except requests.exceptions.RequestException as e:
#     print(f"Произошла ошибка при выполнении запроса: {e}")
# # Это общий класс ошибок requests

'''POST'''

# import requests
#
# # делаем словарь для отправки
# data = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }
#
# # отправляем наш запрос
# response = requests.post(
#     'https://restful-booker.herokuapp.com/booking', json=data)
#
# print(response.json())

