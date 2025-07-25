'''data'''


'''Словарь, или список кортежей'''

'''словарь в data'''
# import requests
#
# url = "https://httpbin.org/post"
# data = {"key1": "value1", "key2": "value2"}
# response = requests.post(url, data=data) # requests сам кодирует словарь в x-www-form-urlencoded
# print(response.request.body) # Показывает закодированное тело запроса
# print(response.text)

'''В этом случае requests автоматически кодирует словарь data в строку вида key1=value1&key2=value2.'''


'''Можно также использовать список кортежей:'''

# data = [("key1", "value1"), ("key2", "value2")]
# response = requests.post(url, data=data)

'''Произвольная строка (str или bytes):'''

# import requests
#
# url = "https://httpbin.org/post"
# data = "<xml><data>some data</data></xml>"  # Отправка XML
# response = requests.post(url, data=data)
# print(response.request.body) # тело исходного запроса (request body) из объекта Response
# print(response.text)
#
# data_bytes = b"raw bytes data"
# response_bytes = requests.post(url, data=data_bytes)
# print(response_bytes.request.body)
# print(response_bytes.text)

'''Здесь данные отправляются как есть, без кодирования. Важно правильно установить заголовок Content-Type, 
чтобы сервер знал, как интерпретировать данные (например, Content-Type: application/xml или Content-Type: text/plain).'''




'''JSON'''

# import requests
#
# url = "https://httpbin.org/post"
# data = {"key1": "value1", "key2": "value2"}
# response = requests.post(url, json=data) # requests автоматически сериализует в JSON
# print(response.request.body) # Показывает JSON в теле запроса
# print(response.json()) # Декодированный JSON ответ сервера