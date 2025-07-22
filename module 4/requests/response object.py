# import requests
#
# url = "https://httpbin.org/get"
# response = requests.get(url)
#
# print(f"Status Code: {response.status_code}")
# print(f"Headers: {response.headers}")
# print(f"Content (bytes): {response.content}")
# print(f"Text (string): {response.text}")
# print(f"URL: {response.url}")
# print(f"History: {response.history}")
# print(f"Cookies: {response.cookies}")
# print(f"Encoding: {response.encoding}")
# print(f"Elapsed Time: {response.elapsed}")
# print(f"Request: {response.request}")
# print(f"Reason: {response.reason}")

'''> Объект `Response` имеет следующие основные атрибуты и методы:
> 
> - `status_code`: Код статуса HTTP-ответа (например, 200 OK, 404 Not Found, 500 Internal Server Error)
> - `headers`: Словарь, содержащий заголовки ответа
> - `content`: Содержимое ответа в виде байтовой строки (`bytes`)
> - `text`: Содержимое ответа в виде строки Unicode (получается путем декодирования `content` с использованием определенной кодировки)
> - `json()`: Метод для декодирования JSON-ответа в объект Python (словарь или список)
> - `raw`: Необработанный ответ от сервера (объект `urllib3.response.HTTPResponse`)
> - `url`: URL-адрес, на который был отправлен запрос
> - `history`: Список объектов `Response`, представляющих историю перенаправлений (если они были)
> - `cookies`: Объект `RequestsCookieJar`, содержащий куки, установленные сервером
> - `encoding`: Кодировка, используемая для декодирования `content` в `text`
> - `elapsed`: Объект `datetime.timedelta`, представляющий время, затраченное на выполнение запроса
> - `request`: Объект `PreparedRequest`, представляющий отправленный запрос
> - `reason`: Текстовое описание статуса (например, "OK", "Not Found")'''

# import requests
#
# url = "https://httpbin.org/get"  # Простой эндпоинт, возвращающий информацию о запросе
# response = requests.get(url)
#
# if response.status_code == 200: # Проверяем успешность запроса
#     print(f"Текст ответа:\n{response.text}") # Выводим текст ответа
# else:
#     print(f"Ошибка запроса: {response.status_code}")
#     print(f"Текст ошибки:\n{response.text}") # Выводим текст ошибки, если она

'''Изменение кодировки'''

# import requests
#
# url = "https://httpbin.org/encoding/utf8"  # Пример, где httpbin сообщает кодировку utf-8
# response = requests.get(url)
#
# print(f"Кодировка до изменения: {response.encoding}")
# print(f"Текст до изменения:\n{response.text}")
#
# response.encoding = 'utf-8'  # Явно устанавливаем utf-8 (в данном случае это избыточно, так как httpbin уже указал эту кодировку)
# print(f"Кодировка после изменения: {response.encoding}")
# print(f"Текст после изменения:\n{response.text}")
#
# url_latin = "https://httpbin.org/encoding/utf8" # Пример, где мы *ошибочно* предполагаем latin1
# response_latin = requests.get(url_latin)
# response_latin.encoding = 'latin1' # *Неправильная* кодировка, приведет к искажению текста
# print(f"Текст с (неправильной) кодировкой latin1:\n{response_latin.text}")
#
# # Правильный подход:
# response_latin_correct = requests.get(url_latin)
# response_latin_correct.encoding = response_latin_correct.apparent_encoding # используем apparent_encoding
# print(f"Текст с (автоматически определенной) кодировкой:\n{response_latin_correct.text}")

'''JSON'''

# import requests
#
# url = "https://httpbin.org/json"
# response = requests.get(url)
# data = response.json()
# print(type(data))
# print(data)
# print(data['slideshow']['author'])
#
# try:
#     data = response.json()  # Пытаемся декодировать JSON
#     print(type(data))  # Выведет <class 'dict'>
#     print(data)  # Выведет содержимое JSON
#     print(data['slideshow']['author']) # Доступ к вложенным элементам
# except requests.exceptions.JSONDecodeError as e:
#     print(f"Ошибка декодирования JSON: {e}")
#     print(f"Текст ответа: {response.text}") # Выводим текст ответа для отладки
# except Exception as e:
#     print(f"Другая ошибка: {e}")


# import requests
#
# urls = [
#     "https://httpbin.org/json",  # Нормальный JSON
#     "https://httpbin.org/status/204", # Пустой ответ
#     "https://httpbin.org/status/500",  # Ошибка 500
#     "https://httpbin.org/html", # HTML
# ]
#
# for url in urls:
#     print(f"URL: {url}")
#     response = requests.get(url)
#     print(f"Status code: {response.status_code}")
#     try:
#         data = response.json()
#         print(f"JSON data: {data}")
#     except requests.exceptions.JSONDecodeError:
#         print(f"Ошибка декодирования JSON. Текст ответа: {response.text}") # Выводим первые 100 символов
#     except Exception as e:
#         print(f"Другая ошибка: {e}")
#     print("-" * 20)


import requests
url = 'https://httpbin.org/json'
response = requests.get(url)
print(response.status_code)
print(response.json())
print(response.headers) #Заголовки ответа
print(response.request.headers) #Заголовки запроса