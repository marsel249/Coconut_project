import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator


class TestDelMoviesAPI:

    def test_del_movie(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание и удаление фильма'''

        mov_id = api_manager.movies_api.info_id(create_movie)
        response = api_manager.movies_api.get_movie_by_id(mov_id)
        mov_del = api_manager.movies_api.delete_movie(mov_id, expected_status=200)
        response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)

        assert response.status_code == 404, "Фильм не удален"


    def test_NEGATIVE_del_ithout_auth(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание и удаление фильма, без прав'''

        del_auth = api_manager.auth_api.del_auth()

        mov_id = api_manager.movies_api.info_id(create_movie)
        response = api_manager.movies_api.get_movie_by_id(mov_id)
        mov_del = api_manager.movies_api.delete_movie(mov_id, expected_status=401)
        response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=200)

        assert response.status_code == 200, "Фильм удален"

    def test_NEGATIVE_del_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, удаление несуществующего фильма'''
        # Узнаем id созданного фильма, добавляем число, проверяем, что такого фильма не существует, пытаемся его удалить.
        mov_id = api_manager.movies_api.info_id(create_movie)+10000
        response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)
        mov_del = api_manager.movies_api.delete_movie(mov_id, expected_status=404)
        # response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)

        assert response.status_code == 404, "Фильм не удален"

