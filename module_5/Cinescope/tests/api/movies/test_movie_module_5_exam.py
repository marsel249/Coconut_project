import pytest

from module_4.Cinescope.conftest import create_movie
from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.utils.data_generator import DataGenerator
from module_5.Cinescope.models.base_models import MovieTestData, MovieResponse, ErrorResponse
from module_5.Cinescope.db_requester.models import MovieDBModel
from sqlalchemy.exc import NoResultFound
import allure

@allure.epic('Тестирование взаимодействия с БД movies, валидация тестовых данных и респонсов')
class TestPostMoviesAPI:

    def test_double_create_movie_new_method(self, super_admin_token, api_manager, db_session):
        '''Попытка создать один и тот же фильм, дважды, новый метод

        Тут парсим тестовую дату, с помощью пайдентик модели, проверяем есть ли фильм в БД, парсим моделью респонс с ошибкой'''

        movie_data = DataGenerator.generate_random_movie()
        movie_data = MovieTestData(**movie_data)
        create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=201, token=super_admin_token)
        create_movie_id = create_movie.json()['id']
        db_session.query(MovieDBModel).filter_by(id=create_movie_id)
        create_second_movie = api_manager.movies_api.create_movie(movie_data, expected_status=409, token=super_admin_token)
        ErrorResponse.model_validate(create_second_movie.json())

    def test_get_all_movie(self, api_manager):
        '''В тесте, запрашиваем все фильмы, парсим пайдентик моделью'''
        get_movies = api_manager.movies_api.get_all_movies()
        MovieResponse.model_validate(get_movies.json())

    @pytest.mark.parametrize('locations,min_price,genre_id', [
        ('SPB', 500, 5),
        ('MSK', 100, 1),
        ('SPB', 900, 6),
        ('MSK', 1, 10)
    ], ids=['tes1', 'test2', 'test3', 'test4'])
    def test_get_filter_movies(self, api_manager, filter_params, locations, min_price, genre_id):
        '''Тест на запрос разных фильмов с параметризацией, парсим тестовую дату и ответ моделью пайдентика'''
        movie_data = DataGenerator.generate_random_movie()
        filter_params['locations'] = locations
        filter_params['min_price'] = min_price
        filter_params['genreId'] = genre_id
        MovieTestData(**movie_data)
        response = api_manager.movies_api.get_all_movies(**filter_params, expected_status=200)
        MovieResponse.model_validate(response.json())

    def test_del_movie(self, api_manager, super_admin_auth, db_session, create_movie):
        '''Находим фильм созданный фикстурой, в базе по id, удаляем его запросом, ищем в базе по id,
        дополнительно проверяем гет запросом(излишне?)'''
        movie_id = api_manager.movies_api.info_id(create_movie)
        db_session.query(MovieDBModel).filter_by(id=movie_id).one()
        api_manager.movies_api.delete_movie(movie_id, expected_status=200)
        with pytest.raises(NoResultFound):
            db_session.query(MovieDBModel).filter_by(id=movie_id).one()
        api_manager.movies_api.get_movie_by_id(movie_id, expected_status=404)


        '''Переделал первый тест под аллюр'''
    @allure.story('Попытка создание дубликата фильма')
    @allure.description("""
    Проверяем, что API не позволяет создать дубликат фильма с тем же названием.
    Шаги:
    1. Генерируем рандомный фильм
    2. Валидируем, с помощью модели
    3. Создаем фильм в базе, с помощью запроса
    4. Получаем id фильма
    5. Находим фильм по id в базе данных
    6. Пытаемся создать новый фильм с помощью запроса (ошибка, 409)
    7. Валидируем ответ с ошибкой, с помощью модели
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('qa_test_allure', 'QA_name')
    @allure.title('Double movie')

    def test_double_create_movie_new_method_with_allure(self, super_admin, super_admin_token, api_manager, db_session):

        with allure.step('Генерируем рандомный фильм'):
            movie_data = DataGenerator.generate_random_movie()
        with allure.step('Валидируем, с помощью модели'):
            movie_data = MovieTestData(**movie_data)
        with allure.step('Создаем фильм в базе, с помощью запроса'):
            create_movie = api_manager.movies_api.create_movie(movie_data, expected_status=201, token=super_admin_token)
        with allure.step('Получаем id фильма'):
            create_movie_id = create_movie.json()['id']
        with allure.step('Находим фильм по id в базе данных'):
            db_session.query(MovieDBModel).filter_by(id=create_movie_id)
        with allure.step('Пытаемся создать новый фильм с помощью запроса (ошибка, 409)'):
            #create_second_movie = api_manager.movies_api.create_movie(movie_data, expected_status=409, token=super_admin_token)
            # #Запрос реализован, через токен из фикстуры
            create_second_movie = super_admin.api.movies_api.create_movie(movie_data, expected_status=409)
            #Реализация, другим методом, ролевая модель
        with allure.step('Валидируем ответ с ошибкой, с помощью модели'):
            ErrorResponse.model_validate(create_second_movie.json())



