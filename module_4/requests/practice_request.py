'''### Задание 1

Напишите тест, который создает бронирование (запрос который использовался в теме про POST запросы)

1. URL по которому обращаемся положить в переменную `URL` чтобы каждый раз не писать/копировать/вставлять его
2. Поскольку это тест, то нужно соответственно сделать asserts для проверки
Пусть это будет “ответ от сервера == 200”'''

# import requests
#
# data = {
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : True,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }
#
# URL = 'https://restful-booker.herokuapp.com/booking'
#
# def test_testresponse():
#     response = requests.post(f'{URL}', json=data)
#     print(response.status_code)
#     print('lalalala')
#     assert response.status_code == 200


'''Сделать апгрейд теста
После создания бронирования, из тела ответа от сервера нужно получить id бронирования

В тесте выполнить запрос get, где в пути будет указан id бронирования. 
Ассертами убедиться, что ответ успешен, а имя совпадает с тем, что было отправлено при пост запросе.'''

# import requests
#
# data = {
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : True,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }
#
# URL = 'https://restful-booker.herokuapp.com/booking/'
#
# def test_testresponse():
#     response = requests.post(f'{URL}', json=data)
#     assert response.status_code == 200
#     assert 'bookingid' in response.json(), "'bookingid' not in response"
#     data_ID = response.json()['bookingid']
#
#     response = requests.get(f'{URL}{data_ID}')
#     assert response.status_code == 200
#     assert data['firstname'] in response.json()['firstname']








'''Черновик, рабочее - выше'''

'''# def test_testresponse():
#     response = requests.post(f'{URL}', json=data)
#     # print(response.status_code)
#     # print('Просто тестовый текст')
#     assert response.status_code == 200
#     assert 'bookingid' in response.json(), "'bookingid' not in response"
#     data_ID = response.json()['bookingid']
#
#     response = requests.get(f'{URL}{data_ID}')
#     assert response.status_code == 200
#     # print(data['firstname'])
#     # print(response.json())
#     # print(response.json()['firstname'])
#     assert data['firstname'] in response.json()['firstname']



# response = requests.post(URL, json=data)
# # response.raise_for_status()
# print(response.status_code)
# assert response.status_code == 200
#
# response_json = response.json()
# print(response_json)
# assert 'bookingid' in response_json
# data_json = response.json()['bookingid'] # ID user
# print(data_json)
#
# response = requests.get(f'{URL}{data_json}')
# assert response.status_code == 200
# print(data['firstname'])
# print(response.json())
# print(response.json()['firstname'])
# assert data['firstname'] in response.json()['firstname']'''

