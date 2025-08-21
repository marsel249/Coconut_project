# Modul_4\Cinescope\tests\api\test_other_api.py
from pytz import timezone
from module_5.Cinescope.utils.data_generator import DataGenerator
from module_5.Cinescope.db_requester.models import MovieDBModel
import datetime


def test_create_delete_movie(api_manager, super_admin_token, db_session_after_close):
    # как бы выглядел SQL запрос
    """SELECT id, "name", price, description, image_url, "location", published, rating, genre_id, created_at
       FROM public.movies
       WHERE name='Test Moviej1h8qss9s5';"""

    movie_name = f"Test Movie{DataGenerator.generate_random_string(10)}"
    movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)

    # проверяем что до начала тестирования фильма с таким названием нет
    assert movies_from_db.count() == 0, "В базе уже присутствует фильм с таким названием"

    movie_data = {
        "name": movie_name,
        "price": 500,
        "description": "Описание тестового фильма",
        "location": "MSK",
        "published": True,
        "genreId": 3
    }

    auth = api_manager.auth_api.update_session_headers_with_token(super_admin_token)

    response = api_manager.movies_api.create_movie(movie_data=movie_data)

    assert response.status_code == 201, "Фильм должен успешно создаться"
    response = response.json()

    # проверяем после вызова api_manager.movies_api.create_movie в базе появился наш фильм
    movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
    assert movies_from_db.count() == 1, "В базе уже присутствует фильм с таким названием"

    movie_from_db = movies_from_db.first()
    # можете обратить внимание что в базе данных етсь поле created_at которое мы не здавали явно
    # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
    assert movie_from_db.created_at >= (
                datetime.datetime.now(timezone('UTC')).replace(tzinfo=None) - datetime.timedelta(
            minutes=5)), "Сервис выставил время создания с большой погрешностью"

    # Берем айди фильма который мы только что создали и  удаляем его из базы через апи
    # Удаляем фильм
    delete_response = api_manager.movies_api.delete_movie(movie_id=response["id"], expected_status=200)
    assert delete_response.status_code == 200, "Фильм должен успешно удалиться"

    # проверяем что в конце тестирования фильма с таким названием действительно нет в базе
    movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
    assert movies_from_db.count() == 0, "Фильм небыл удален из базы!"
