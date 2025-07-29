import pytest
import requests
from module_4.Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.api.api_manager import ApiManager
from module_4.requests.Session import response


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
                assert movie["location"] == filter_params["locations"], f"Локация фильма {movie['id']} не соответствует фильтру"
            # x = movie["published"], переменная для отладки
            # y = filter_params["published"]
            if "published" in filter_params:
                assert movie["published"] == filter_params["published"], f"Статус публикации фильма {movie['id']} не соответствует фильтру"

            if "min_price" in filter_params:
                assert movie["price"] < filter_params["min_price"], f"Цена фильма {movie['id']} меньше min_price"

            if "max_price" in filter_params:
                assert movie["price"] > filter_params["max_price"], f"Цена фильма {movie['id']} больше max_price"

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


    def test_del_movie(self, api_manager: ApiManager, super_admin_auth, create_movie):
        '''создание и удаление фильма'''

        # response = super_admin_auth()
        # response = create_movie()
        # response_data = response.json()
        # id_response = response_data['id']
        # response = api_manager.movies_api.get_movie_by_id(id_response)
        # response = api_manager.movies_api.delete_movie(id_response)
        # response = api_manager.movies_api.get_movie_by_id(id_response)
        #
        # assert response.status_code == 404

    def test_patch_movie(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie'''

        # response = super_admin_auth()
        # response = create_movie()
        # response_data = response.json()
        # id_response = response_data['id']
        # response = api_manager.movies_api.update_movie(id_response, patch_movie_data)
        # response = api_manager.movies_api.get_movie_by_id(id_response)
        # new_response_data = response.json()
        #
        # assert new_response_data == response_data


