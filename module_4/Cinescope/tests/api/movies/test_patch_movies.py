import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator

class TestPatchMoviesAPI:

    def test_patch_movie(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie'''

        first_id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(first_id)
        response = api_manager.movies_api.update_movie(first_id, patch_movie_data)
        second_id = response.json()['id']
        response = api_manager.movies_api.get_movie_by_id(second_id)
        assert response.json() != first_response.json(), "Данные фильма не изменились"


    def test_NEGATIVE_patch_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):

        '''NEGATIVE patch movie, empty data'''

        data = {}
        id_movie = create_movie.json()['id']
        before_response = api_manager.movies_api.get_movie_by_id(id_movie)
        response = api_manager.movies_api.update_movie(id_movie, data)
        after_response = api_manager.movies_api.get_movie_by_id(id_movie)

        assert before_response.json() == after_response.json()


# data = {"authorization": "Bearer "}
#         clear_token = CustomRequester._update_session_headers(**data)