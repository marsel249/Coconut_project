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
        '''создание фильма, запрос фильма по id'''


        first_id = api_manager.movies_api.info_id(create_movie) #тут получаем id созданного фикстурой фильма
        response = api_manager.movies_api.get_movie_by_id(first_id) #тут делаем гет, запрашиваем фильм
        second_id = api_manager.movies_api.info_id(response) #Сравниваем id полученный при создании, id запрошенного фильма

        assert first_id == second_id

    def test_get_id_movie(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма c несуществующим id'''


        first_id = api_manager.movies_api.info_id(create_movie) #тут получаем id созданного фикстурой фильма
        response = api_manager.movies_api.get_movie_by_id(first_id+10000, expected_status=404) #тут делаем гет, запрашиваем фильм

        assert response.status_code == 404




