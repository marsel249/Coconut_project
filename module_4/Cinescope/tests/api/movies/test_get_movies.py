import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator

class TestGetMoviesAPI:
    def test_get_all_movies(self, api_manager: ApiManager):
        """
        Тест на получение фильмов, без параметров
        """

        response = api_manager.movies_api.get_all_movies()
        response_data = response.json()

        # Проверки
        assert "movies" in response_data, "В ответе нет 'movies'"
        assert isinstance(response_data["movies"], list), "movies должен быть списком"

    def test_get_filter_movies(self, api_manager: ApiManager, filter_params):
        """
        Тест на получение фильмов, с заданными параметрами.
        """

        response = api_manager.movies_api.get_all_movies(**filter_params)
        response_data = response.json()

        # Проверки
        assert "movies" in response_data, "В ответе нет 'movies'"
        assert isinstance(response_data["movies"], list), "movies должен быть списком"
        assert response_data['pageSize'] == filter_params['pageSize'], "Количество страниц не совпадает"
        assert response_data['page'] == filter_params['page'], "Страница не совпадает"

        for movie in response_data["movies"]:

            if "genreId" in filter_params and filter_params["genreId"] is not None:
                assert "genreId" in movie, f"Фильм {movie.get('id', '?')} не содержит genreId"
                assert movie["genreId"] == filter_params["genreId"], (
                f"Фильм ID {movie['id']} имеет genreId={movie['genreId']}, "
                f"ожидалось {filter_params['genreId']}")

            if "locations" in filter_params and filter_params["locations"]:
                assert movie["location"] == filter_params["locations"], f"Локация, не соответствует фильтру"
            if "published" in filter_params:
                assert str(movie["published"]).lower() == filter_params["published"], f"Статус публикации, не соответствует фильтру"

            if "min_price" in filter_params:
                assert movie["price"] >= filter_params["min_price"], f"Цена фильма {movie['id']} меньше min_price"

            if "max_price" in filter_params:
                assert movie["price"] <= filter_params["max_price"], f"Цена фильма {movie['id']} больше max_price"

    def test_NEGATIVE_get_page_1(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы > 20.
        """

        filter_params['pageSize'] = random.randint(21, 100)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_get_page_2(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы = 0.
        """

        filter_params['pageSize'] = 0
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_get_page_3(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c отрицательны числом.
        """

        filter_params['pageSize'] = random.randint(-10, -1)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_get_page_4(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page - str.
        """

        filter_params['pageSize'] = DataGenerator.generate_random_word()
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_get_page_5(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page - float.
        """

        filter_params['pageSize'] = random.uniform(1, 20)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_location_1(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c неверной локацией.
        """

        filter_params['locations'] = DataGenerator.generate_random_city()
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_location_2(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c неверной локацией.
        """

        filter_params['locations'] = random.randint(-100, 100)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_page_1(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page = 0.
        """

        filter_params['page'] = 0
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_page_2(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page < 0.
        """

        filter_params['page'] = random.randint(-10, -1)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_page_3(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page - str.
        """

        filter_params['page'] = DataGenerator.generate_random_word()
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_page_4(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c page - float.
        """

        filter_params['page'] = random.uniform(1,20)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_min_price_1(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c min_price < 0.
        """

        filter_params['min_price'] = random.randint(-10, -1)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_max_price_2(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c max_price < min_price.
        """
        num_max = 1
        num_min = 0

        while num_max > num_min:
            num_min = random.randint(0, 10000)
            num_max = random.randint(0, 10000)

        filter_params['min_price'] = num_min
        filter_params['max_price'] = num_max
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert response.status_code == 400


    def test_NEGATIVE_wrong_genre_id_1(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c genreId = 0.
        """

        filter_params['genreId'] = 0
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_genre_id_2(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c genreId - строка.
        """

        filter_params['genreId'] = DataGenerator.generate_random_word()
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400

    def test_NEGATIVE_wrong_genre_id_3(self, api_manager: ApiManager, filter_params):
        """
        Тест на поиск страницы c genreId - float.
        """

        filter_params['genreId'] = random.uniform(1,10)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response.status_code == 400


