import random

from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.utils.data_generator import DataGenerator

class TestPostMoviesAPI:

    def test_double_create_movie_new_method(self, super_admin):
        '''Попытка создать один и тот же фильм, дважды, новый метод'''

        movie_data = DataGenerator.generate_random_movie()
        create_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=201)
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