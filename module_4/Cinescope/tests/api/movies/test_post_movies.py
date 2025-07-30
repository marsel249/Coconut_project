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


    def test_NEGATIVE_without_auth(self, api_manager: ApiManager):
        '''создание фильма, без аутенфикации'''

        data = {"authorization": "Bearer "}

        clear_token = api_manager.session.headers.update(data)

        movie_data = DataGenerator.generate_random_movie()
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=401)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 401

    def test_NEGATIVE_double_create(self, api_manager: ApiManager, super_admin_auth):
        '''Попытка создать один и тот же фильм, дважды'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=201)
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=409)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 409


    def test_NEGATIVE_wrong_name_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c name < 3 символов'''

        name = DataGenerator.generate_random_name(2)

        movie_data = DataGenerator.generate_random_movie()
        movie_data['name'] = name

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_name_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c name - empty'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['name'] = ''

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_price_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c price - str'''


        movie_data = DataGenerator.generate_random_movie()
        movie_data['price'] = DataGenerator.generate_random_word()

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400


    def test_NEGATIVE_wrong_price_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c price - 0'''


        movie_data = DataGenerator.generate_random_movie()
        movie_data['price'] = 0

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_price_3(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c price < 0'''


        movie_data = DataGenerator.generate_random_movie()
        movie_data['price'] = random.randint(-100, -1)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_price_4(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c price - empty'''


        movie_data = DataGenerator.generate_random_movie()
        movie_data['price'] = ''

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_url_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c url - empty'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['imageUrl'] = ''

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_url_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c url - число
        !!! тест падает, через свагер с 400, здесь ошибка 500, уточнить'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['imageUrl'] = random.randint(-100, 100)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=500)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 500

    def test_NEGATIVE_wrong_discription_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c описанием - 5< символа'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['description'] = DataGenerator.generate_random_name(random.randint(1,4))

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_discription_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c описанием - empty'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['description'] = ''

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_discription_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c описанием - число'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['description'] = random.randint(-100,100)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_location_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c location - empty'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['location'] = ''

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_location_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c location - random.srt'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['location'] = DataGenerator.generate_random_word()

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_location_3(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c location - число'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['location'] = random.randint(-100,100)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_published_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c published - число'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['published'] = random.randint(-100,100)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_published_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c published - str'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['published'] = DataGenerator.generate_random_word()

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_genreId_1(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c genreId - 0'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['genreId'] = 0

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_genreId_2(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c genreId - str'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['genreId'] = DataGenerator.generate_random_word()

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400

    def test_NEGATIVE_wrong_genreId_3(self, api_manager: ApiManager, super_admin_auth):
        '''создание фильма, c genreId - float'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data['genreId'] = random.uniform(1,10)

        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=400)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert isinstance(create_movie.json()["message"], list), "message должен быть списком"
        assert create_movie.status_code == 400
