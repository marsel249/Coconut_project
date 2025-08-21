import random
from tkinter.font import names
import requests

import pytest

from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.utils.data_generator import DataGenerator

class TestPostMoviesAPI:

    def test_double_create_movie_new_method(self, super_admin):
        '''Попытка создать один и тот же фильм, дважды, новый метод'''

        movie_data = DataGenerator.generate_random_movie()
        super_admin.api.movies_api.create_movie(movie_data, expected_status=201)
        create_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=409)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 409

    def test_double_create_movie_old_method(self, api_manager: ApiManager, super_admin_auth):
        '''Попытка создать один и тот же фильм, дважды, старый метод'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=201)
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=409)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 409

    @pytest.mark.slow
    def test_create_movie_without_admin_role(self, common_user):
        '''Попытка создать фильм с ролью user'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = common_user.api.movies_api.create_movie(movie_data, expected_status=403)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 403

    def test_create_movie_with_admin_role(self, admin_user):
        '''Попытка создать фильм с ролью admin'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = admin_user.api.movies_api.create_movie(movie_data, expected_status=403)

        assert "message" in create_movie.json(), "Response не содержит сообщения об ошибке"
        assert create_movie.status_code == 403

    def test_create_movie_with_super_admin_role(self, super_admin):
        '''Попытка создать фильм с ролью super_admin'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=201)

@pytest.mark.parametrize("min_price,max_price,locations,genreId", [
        (1, 1000, 'MSK', 1),
        (1, 1000, 'SPB', 5),
        (1, 1000, 'SPB', 7),
    ], ids=['1 test', '2 test', '3 test'])
def test_get_movies_filter_params(api_manager, min_price, max_price, locations, genreId):
        params = {
            "min_price": min_price,
            "max_price": max_price,
            "locations": locations,
            "genreId": genreId
        }
        response = api_manager.movies_api.get_all_movies(**params).json()

        assert "movies" in response, "В ответе нет 'movies'"
        assert isinstance(response["movies"], list), "movies должен быть списком"

        for movie in response["movies"]:

            if "genreId" in params and params['genreId'] is not None:
                assert "genreId" in movie, '"genreId" нет в movie'
                assert movie["genreId"] == params["genreId"], '"genreId" в выдаче, не соответствует заданному'

            if "locations" in params and params['locations'] is not None:
                assert "location" in movie, '"location" нет в movie'
                assert movie["location"] == params["locations"], '"locations" в выдаче, не соответствует заданному'

            if "max_price" in params:
                assert movie['price'] <= params['max_price'], 'max price в выдаче, больше заданной по условию '

            if "min_price" in params:
                assert movie['price'] >= params['min_price'], 'min price в выдаче, меньше заданной по условию '

@pytest.mark.parametrize("name,price,imageUrl", [
    ('first_name1', 850, 'http://www.exampleurl.com/1.png'),
    ('second_name1', 500, 'http://www.exampleurl.com/2.png'),
    ('third_name1', 1400, 'http://www.exampleurl.com/3.png'),
], ids=['1 test', '2 test', '3 test'])

def test_del_movie(super_admin, name, price, imageUrl):
    """создание и удаление фильма"""
    movie_data = DataGenerator.generate_random_movie()

    movie_data['name'] = name
    movie_data['price'] = price
    movie_data['imageUrl'] = imageUrl

    create_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=201)
    mov_id = super_admin.api.movies_api.info_id(create_movie)
    super_admin.api.movies_api.delete_movie(mov_id, expected_status=200)
    response = super_admin.api.movies_api.get_movie_by_id(mov_id, expected_status=404)
    if response.status_code != 404:
        super_admin.api.movies_api.delete_movie(mov_id)



@pytest.mark.parametrize("role,name,price,imageUrl,expected_status,after_exp_status", [
    ('super_admin', 'first_name_1', 850, 'http://www.exampleurl.com/1.png', 200, 404),
    ('admin_user', 'second_name_1', 500, 'http://www.exampleurl.com/2.png', 200, 404),
    ('common_user', 'third_name_1', 1400, 'http://www.exampleurl.com/3.png', 403, 200),
], ids=['1 test - super admin', '2 test - admin', '3 test - common user'])

def test_del_movie_with_roles(role, super_admin, name, price, imageUrl, expected_status, after_exp_status, request):
    """создание и удаление фильма"""
    getrole = request.getfixturevalue(role)
    movie_data = DataGenerator.generate_random_movie()

    movie_data['name'] = name
    movie_data['price'] = price
    movie_data['imageUrl'] = imageUrl

    create_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=201)
    mov_id = super_admin.api.movies_api.info_id(create_movie)
    getrole.api.movies_api.delete_movie(mov_id, expected_status=expected_status)
    super_admin.api.movies_api.get_movie_by_id(mov_id, expected_status=after_exp_status)
    if expected_status != 200:
        super_admin.api.movies_api.delete_movie(mov_id)

def test_del_movie_(super_admin, admin_user):
    movie = DataGenerator.generate_random_movie()
    response = super_admin.api.movies_api.create_movie(movie)
    movie_id = super_admin.api.movies_api.info_id(response)
    # super_admin.api.movies_api.delete_movie(movie_id, expected_status=200)
    admin_user.api.movies_api.delete_movie(movie_id, expected_status=200)
    admin_user.api.movies_api.get_movie_by_id(movie_id, expected_status=404)

def test_admin_creation_logs(admin_user):
    assert True

@pytest.mark.skipif(reason='off')
def test_admin_creation_logs_mark(admin_user):
    assert True

def test_db_fixture(db_session_with_create_user):
    assert True

def test_db_fixture_(db_session_after_close):
    assert True


