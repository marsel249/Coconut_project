
import requests

# def test_google():
#     response = requests.get("https://www.google.com")
#     assert response.status_code == 200

# pytest
# pytest --html=report.html

# import requests
#
# # Отправляем GET-запрос
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#
# # Проверяем статус ответа
# print("Статус-код:", response.status_code)
#
# # Выводим тело ответа
# print("Ответ:", response.json())

# import pytest
# import requests
#
# # Фикстура для базового URL
# @pytest.fixture
# def base_url():
#     return "https://jsonplaceholder.typicode.com"
#
# # Тестовый метод
# def test_get_post(base_url):
#     response = requests.get(f"{base_url}/posts/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1

from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()

# Получаем переменные
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")

print("Базовый URL:", base_url)
print("API-ключ:", api_key)
