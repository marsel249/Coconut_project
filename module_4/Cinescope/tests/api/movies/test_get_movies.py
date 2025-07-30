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
        Тест на получение фильмов, с заданными параметрами пагинации.
        """

        response = api_manager.movies_api.get_all_movies()
        response_data = response.json()

        # Проверки
        assert "movies" in response_data, "В ответе нет 'movies'"
        assert isinstance(response_data["movies"], list), "movies должен быть списком"

    def test_get_filter_movies(self, api_manager: ApiManager, filter_params):
        """
        Тест на получение фильмов, с заданными параметрами пагинации.
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
            # x = movie["published"], переменная для отладки
            # y = filter_params["published"]
            if "published" in filter_params:
                assert str(movie["published"]).lower() == filter_params["published"], f"Статус публикации, не соответствует фильтру"

            if "min_price" in filter_params:
                assert movie["price"] >= filter_params["min_price"], f"Цена фильма {movie['id']} меньше min_price"

            if "max_price" in filter_params:
                assert movie["price"] <= filter_params["max_price"], f"Цена фильма {movie['id']} больше max_price"

    def test_NEGATIVE_get_filter_movies1(self, api_manager: ApiManager, filter_params):
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



