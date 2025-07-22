'''Можно модифицировать параметры, в рамках сессии'''
# import requests
#
# s = requests.Session()
# s.headers.update({'User-Agent': 'My Custom Bot'}) # Постоянный заголовок
# s.auth = ('user', 'password') # Постоянная аутентификация
#
# response = s.get('https://httpbin.org/headers')
# print(response.json())
#
# response2 = s.post('https://httpbin.org/post', json={"data": "test"})
# print(response2.json())

'''Устанавливаем куки, они хранятся в рамках сессии'''
# import requests
#
# s = requests.Session()
#
# # Первый запрос (сервер устанавливает cookie)
# response1 = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# print(response1.text)
#
# # Второй запрос (cookie автоматически отправляется)
# response2 = s.get('https://httpbin.org/cookies')
# print(response2.json()) # Видим, что cookie был отправлен

'''Если использовать параметры на уровне метода, а не модификацией сессии - параметры в других запросах не работают'''
# import requests
# s = requests.Session()
#
# # Указываем cookie для первого запроса
# r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)
# # Вывод: '{"cookies": {"from-my": "browser"}}'
#
# # Второй запрос не использует cookie
# r = s.get('https://httpbin.org/cookies')
# print(r.text)
# # Вывод: '{"cookies": {}}'


# import requests
# s = requests.Session()
# s.cookies.update({'from-my': 'browser'}) # Указываем cookie для всей сессии
# r = s.get('https://httpbin.org/cookies')
# print(r.text)
#
# r = s.get('https://httpbin.org/cookies')
# print(r.text)
# print(s.cookies.get_dict()) # Проверяем куки сессии



# import requests
#
# s = requests.Session()
# print("Начальные куки сессии:", s.cookies.get_dict())  # {}
#
# # Первый запрос
# r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print("Куки после 1 запроса:", s.cookies.get_dict())  # {}
#
# # Второй запрос
# r = s.get('https://httpbin.org/cookies')
# print("Куки после 2 запроса:", s.cookies.get_dict())  # {}

'''Сохранение кук между запросами'''
# import requests
#
# s = requests.Session()
#
# # Способ 1: Вручную добавить в сессию
# s.cookies.set('from-my', 'browser')
#
# # Способ 2: Использовать hooks (более правильный подход)
# def save_cookies(response, *args, **kwargs):
#     if 'cookies' in response.json():
#         s.cookies.update(response.json()['cookies'])
#
# s.hooks['response'] = save_cookies
#
# r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# r = s.get('https://httpbin.org/cookies')  # Теперь куки будут



import requests
import time
import logging
logging.basicConfig(level=logging.DEBUG)  # Покажет все сетевые операции

url = "https://httpbin.org/get"
num_requests = 10

print("Запросы с использованием сессии:")
start_time = time.time()

session = requests.Session()  # Создаем сессию
try:
    for i in range(num_requests):
        response = session.get(url)
        response.raise_for_status()
except Exception as e:
    print(f"ошибка: {e}")
finally:
    session.close()  # закрываем сессию
end_time = time.time()
print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")

# Запросы БЕЗ использования сессии:
print("Запросы БЕЗ использования сессии:")
start_time = time.time()
try:
    for i in range(num_requests):
        response = requests.get(url)
        response.raise_for_status()
except Exception as e:
    print(f"Ошибка: {e}")
end_time = time.time()
print(f"Время выполнения без сессии: {end_time - start_time:.4f} секунд")
