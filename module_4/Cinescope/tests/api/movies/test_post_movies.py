import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator



class TestPostMoviesAPI:

    def test_create_film(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма по id, проверка, что фильм создан'''

        first_id = api_manager.movies_api.info_id(create_movie) #тут получаем id созданного фикстурой фильма
        response = api_manager.movies_api.get_movie_by_id(first_id) #тут делаем гет, запрашиваем фильм
        second_id = api_manager.movies_api.info_id(response) #Сравниваем id полученный при создании, id запрошенного фильма

        assert first_id == second_id
        assert create_movie.json()['name'] == response.json()['name']
        assert create_movie.json()['imageUrl'] == response.json()['imageUrl']
        assert create_movie.json()['price'] == response.json()['price']
        assert create_movie.json()['description'] == response.json()['description']
        assert create_movie.json()['location'] == response.json()['location']
        assert create_movie.json()['published'] == response.json()['published']
        assert create_movie.json()['genreId'] == response.json()['genreId']


    def test_NEGATIVE_create_film_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c name < 3 символов'''

        name = DataGenerator.generate_random_name(2)

        movie_data = DataGenerator.generate_random_movie()
        movie_data['name'] = name

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

