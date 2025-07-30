import random

import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response
from module_4.Cinescope.utils.data_generator import DataGenerator



class TestAuthAPI:
    def test_register_user(self, api_manager: ApiManager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"





    def test_get_all_movies(self, api_manager: ApiManager):
        """
        Тест на получение фильмов, с заданными параметрами пагинации.
        """
        # response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)
        response = api_manager.movies_api.get_all_movies()
        response_data = response.json()

        # Проверки
        assert "movies" in response_data, "В ответе нет 'movies'"
        assert isinstance(response_data["movies"], list), "movies должен быть списком"

    def test_get_filter_movies(self, api_manager: ApiManager, filter_params):
        """
        Тест на получение фильмов, с заданными параметрами пагинации.
        """
        # response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)
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
        # response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)
        filter_params['pageSize'] = random.randint(21, 100)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=400)
        response_data = response.json()

        # Проверки
        assert "message" in response_data, "Response не содержит сообщения об ошибке"
        assert isinstance(response_data["message"], list), "message должен быть списком"
        assert response_data.status_code == 400



    def test_create_film(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание фильма, запрос фильма по id, проверка, что фильм создан'''

        # response_data = create_movie.json()
        # id_response = response_data['id']
        # response = api_manager.movies_api.get_movie_by_id(id_response)
        # response_data = response.json()
        # if 'id' in response_data:
        #     assert response_data['id'] == id_response

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


    def test_del_movie(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание и удаление фильма'''

        mov_id = api_manager.movies_api.info_id(create_movie)
        response = api_manager.movies_api.get_movie_by_id(mov_id)
        mov_del = api_manager.movies_api.delete_movie(mov_id, expected_status=201)
        response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)

        assert response.status_code == 404, "Фильм не удален"

    def test_NEGATIVE_del_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание и удаление несуществующего фильма'''
        # Узнаем id созданного фильма, добавляем число, проверяем, что такого фильма не существует, пытаемся его удалить.
        mov_id = api_manager.movies_api.info_id(create_movie)+10000
        response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)
        mov_del = api_manager.movies_api.delete_movie(mov_id, expected_status=404)
        # response = api_manager.movies_api.get_movie_by_id(mov_id, expected_status=404)

        assert response.status_code == 404, "Фильм не удален"




    def test_patch_movie(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie'''

        first_id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(first_id)
        response = api_manager.movies_api.update_movie(first_id, patch_movie_data)
        second_id = response.json()['id']
        response = api_manager.movies_api.get_movie_by_id(second_id)
        # x = response.json()
        # y = first_response.json()
        assert response.json() != first_response.json(), "Данные фильма не изменились"


    def test_NEGATIVE_patch_movie_1(self, api_manager: ApiManager, super_admin_auth, create_movie):

        '''NEGATIVE patch movie, empty data'''

        data = {}
        id_movie = create_movie.json()['id']
        before_response = api_manager.movies_api.get_movie_by_id(id_movie)
        response = api_manager.movies_api.update_movie(id_movie, data)
        after_response = api_manager.movies_api.get_movie_by_id(id_movie)

        assert before_response.json() == after_response.json()


