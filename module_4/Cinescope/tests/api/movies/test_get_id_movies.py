import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator



class TestGetIdMoviesAPI:

    def test_get_id_movie(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма по id, сравнение id созданного фильма, и запрошенного'''

        first_id = api_manager.movies_api.info_id(create_movie) #тут получаем id созданного фикстурой фильма
        response = api_manager.movies_api.get_movie_by_id(first_id) #тут делаем гет, запрашиваем фильм
        second_id = api_manager.movies_api.info_id(response) #Сравниваем id полученный при создании, id запрошенного фильма

        assert first_id == second_id

    def test_get_id_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма по id, проверка структуры json'''

        first_id = api_manager.movies_api.info_id(create_movie) #тут получаем id созданного фикстурой фильма
        response = api_manager.movies_api.get_movie_by_id(first_id) #тут делаем гет, запрашиваем фильм
        second_id = api_manager.movies_api.info_id(response) #Сравниваем id полученный при создании, id запрошенного фильма
        create_movie = create_movie.json()
        response = response.json()

        assert first_id == second_id
        assert create_movie['name'] == response['name']
        assert create_movie['imageUrl'] == response['imageUrl']
        assert create_movie['price'] == response['price']
        assert create_movie['description'] == response['description']
        assert create_movie['location'] == response['location']
        assert create_movie['published'] == response['published']
        assert create_movie['genreId'] == response['genreId']

    def test_NEGATIVE_get_id_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма c несуществующим id'''

        first_id = api_manager.movies_api.info_id(create_movie)
        response = api_manager.movies_api.get_movie_by_id(first_id+10000, expected_status=404)

        assert response.status_code == 404

    def test_NEGATIVE_get_id_movie_2(self, api_manager: ApiManager):
        '''создание фильма, запрос фильма c id - str

        Error - 500? '''

        response = api_manager.movies_api.get_movie_by_id(DataGenerator.generate_random_word(), expected_status=500)
        assert response.status_code == 500




