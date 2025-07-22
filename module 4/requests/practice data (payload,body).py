'''Задание 1:
1. Отправить POST запрос, урл и дата ниже, передав payload в параметр json:
(ответ от сервера можно напечатать как print(response.text) )
(посмотреть тело отправки запроса print(response.request.body))
url = '<https://restful-booker.herokuapp.com/booking>'
2. payload = {
3.     "firstname": "Jim",
4.     "lastname": "Brown",
5.     "totalprice": 111,
6.     "depositpaid": True,
7.     "bookingdates": {
8.         "checkin": "2025-01-04",
9.         "checkout": "2025-01-15"
10.     },
11.     "additionalneeds": "Breakfast"
12. }
13.
14. Теперь изменить параметр отправки с json на data
Повторить запрос - ознакомиться с ответом и тем, как был отправлен body в запросе'''

import requests

payload = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-04",
        "checkout": "2025-01-15"
    },
    "additionalneeds": "Breakfast"
}
url = 'https://restful-booker.herokuapp.com/booking'

response = requests.request(method='POST', url=url, json=payload)
assert response.status_code == 200
print(response.status_code)
print(response.text) # ответ сервера
print(response.request.body) # боди отправленного запроса

print(f'\n')
# import requests

# payload = {
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
# url = 'https://restful-booker.herokuapp.com/booking'

response = requests.request(method='POST', url=url, data=payload)
# assert response.status_code == 200
print(response.status_code)
print(response.text) # ответ сервера
print(response.request.body) # боди отправленного запроса


'''
Ответ при отправке json 
200
{"bookingid":258,"booking":{"firstname":"Jim","lastname":"Brown","totalprice":111,"depositpaid":true,"bookingdates":{"checkin":"2025-01-04","checkout":"2025-01-15"},"additionalneeds":"Breakfast"}}
b'{"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": true, "bookingdates": {"checkin": "2025-01-04", "checkout": "2025-01-15"}, "additionalneeds": "Breakfast"}'

Ответ при отправке data 
500
Internal Server Error
firstname=Jim&lastname=Brown&totalprice=111&depositpaid=True&bookingdates=checkin&bookingdates=checkout&additionalneeds=Breakfast
'''

