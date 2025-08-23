# # Modul_4\Cinescope\tests\api\test_other_api.py
# import random
#
# from pytz import timezone
# from module_5.Cinescope.utils.data_generator import DataGenerator
# from module_5.Cinescope.db_requester.models import MovieDBModel, AccountTransactionTemplate
# import datetime
# import pytest
#
#
# def test_create_delete_movie(api_manager, super_admin_token, db_session_after_close):
#     # как бы выглядел SQL запрос
#     """SELECT id, "name", price, description, image_url, "location", published, rating, genre_id, created_at
#        FROM public.movies
#        WHERE name='Test Moviej1h8qss9s5';"""
#
#     movie_name = f"Test Movie{DataGenerator.generate_random_string(10)}"
#     movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
#
#     # проверяем что до начала тестирования фильма с таким названием нет
#     assert movies_from_db.count() == 0, "В базе уже присутствует фильм с таким названием"
#
#     movie_data = {
#         "name": movie_name,
#         "price": 500,
#         "description": "Описание тестового фильма",
#         "location": "MSK",
#         "published": True,
#         "genreId": 3
#     }
#
#     # auth = api_manager.auth_api.update_session_headers_with_token(super_admin_token)
#
#     response = api_manager.movies_api.create_movie(movie_data=movie_data, token=super_admin_token)
#
#     assert response.status_code == 201, "Фильм должен успешно создаться"
#     response = response.json()
#
#     # проверяем после вызова api_manager.movies_api.create_movie в базе появился наш фильм
#     movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
#     assert movies_from_db.count() == 1, "В базе количество фильмов с таким названием != 1 (0, or >1)"
#
#     movie_from_db = movies_from_db.first()
#     # можете обратить внимание что в базе данных етсь поле created_at которое мы не здавали явно
#     # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
#     assert movie_from_db.created_at >= (
#                 datetime.datetime.now(timezone('UTC')).replace(tzinfo=None) - datetime.timedelta(
#             minutes=5)), "Сервис выставил время создания с большой погрешностью"
#
#     # Берем айди фильма который мы только что создали и удаляем его из базы через апи
#     # Удаляем фильм
#     delete_response = api_manager.movies_api.delete_movie(movie_id=response["id"], expected_status=200)
#     assert delete_response.status_code == 200, "Фильм должен успешно удалиться"
#
#     # проверяем что в конце тестирования фильма с таким названием действительно нет в базе
#     movies_from_db = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
#     assert movies_from_db.count() == 0, "Фильм небыл удален из базы!"




#     # Modul_4\Cinescope\tests\api\test_other_api.py
#
# def test_accounts_transaction_template(db_session_after_close: "Session"):
#     # ====================================================================== Подготовка к тесту
#     # Создаем новые записи в базе данных (чтоб точно быть уверенными что в базе присутствуют данные для тестирования)
#
#     stan = AccountTransactionTemplate(user=f"Stas_{random.randint(1000, 10000)}", balance=1000)
#     bob = AccountTransactionTemplate(user=f"Bober_{random.randint(1000, 10000)}", balance=500)
#
#     # Добавляем записи в сессию
#     db_session_after_close.add_all([stan, bob])
#     # Фиксируем изменения в базе данных
#     db_session_after_close.commit()
#
#     def transfer_money(session, from_account, to_account, amount):
#         # пример функции выполняющей транзакцию
#         # представим что она написана на стороне тестируемого сервиса
#         # и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
#         """
#         Переводит деньги с одного счета на другой.
#         :param session: Сессия SQLAlchemy.
#         :param from_account_id: ID счета, с которого списываются деньги.
#         :param to_account_id: ID счета, на который зачисляются деньги.
#         :param amount: Сумма перевода.
#         """
#         # Получаем счета
#         from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
#         to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()
#
#         # Проверяем, что на счете достаточно средств
#         if from_account.balance < amount:
#             raise ValueError("Недостаточно средств на счете")
#
#         # Выполняем перевод
#         from_account.balance -= amount
#         to_account.balance += amount
#
#         # Сохраняем изменения
#         session.commit()
#
#     # ====================================================================== Тест
#     # Проверяем начальные балансы
#     assert stan.balance == 1000
#     assert bob.balance == 500
#
#     try:
#         # Выполняем перевод 200 единиц от stan к bob
#         transfer_money(db_session_after_close, from_account=stan.user, to_account=bob.user, amount=200)
#
#         # Проверяем, что балансы изменились
#         assert stan.balance == 800
#         assert bob.balance == 700
#
#     except Exception as e:
#         # Если произошла ошибка, откатываем транзакцию
#         db_session_after_close.rollback()  # откат всех введеных нами изменений
#         pytest.fail(f"Ошибка при переводе денег: {e}")
#
#     finally:
#         # Удаляем данные для тестирования из базы
#         db_session_after_close.delete(stan)
#         db_session_after_close.delete(bob)
#         # Фиксируем изменения в базе данных
#         db_session_after_close.commit()


# #Удаляем запись с name = 'Bober_9426'
# from sqlalchemy import delete
#
# def test_delite(db_session_after_close: "Session"):
#     name = 'Bober_9426'
#     query = (
#         delete(AccountTransactionTemplate)
#         .where(AccountTransactionTemplate.user == name)
#         .returning(AccountTransactionTemplate.user)
#     )
#
#     db_session_after_close.execute(query).scalar_one_or_none()
#     db_session_after_close.commit()
#
#
#
# def test_accounts_transaction_template_home_work(db_session_after_close: "Session"):
#     # ====================================================================== Подготовка к тесту
#     # Создаем новые записи в базе данных (чтоб точно быть уверенными что в базе присутствуют данные для тестирования)
#
#     stan = AccountTransactionTemplate(user=f"Stas_{random.randint(1000, 10000)}", balance=1000)
#     bob = AccountTransactionTemplate(user=f"Bober_{random.randint(1000, 10000)}", balance=500)
#
#     # Добавляем записи в сессию
#     db_session_after_close.add_all([stan, bob])
#     # Фиксируем изменения в базе данных
#     db_session_after_close.commit()
#
#     def transfer_money(session, from_account, to_account, amount):
#         # пример функции выполняющей транзакцию
#         # представим что она написана на стороне тестируемого сервиса
#         # и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
#         """
#         Переводит деньги с одного счета на другой.
#         :param session: Сессия SQLAlchemy.
#         :param from_account_id: ID счета, с которого списываются деньги.
#         :param to_account_id: ID счета, на который зачисляются деньги.
#         :param amount: Сумма перевода.
#         """
#         # Получаем счета
#         from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
#         to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()
#
#         # Проверяем, что на счете достаточно средств
#         if from_account.balance < amount:
#             raise ValueError("Недостаточно средств на счете")
#
#         # Выполняем перевод
#         from_account.balance -= amount
#         to_account.balance += amount
#
#         # Сохраняем изменения
#         session.commit()
#
#     # ====================================================================== Тест
#     # Проверяем начальные балансы
#     assert stan.balance == 1000
#     assert bob.balance == 500
#
#     try:
#         # Выполняем перевод 1100 единиц от stan к bob, будет ошибка
#         transfer_money(db_session_after_close, from_account=stan.user, to_account=bob.user, amount=1100)
#
#         # Проверяем, что балансы изменились
#         assert stan.balance == 800
#         assert bob.balance == 700
#
#     except Exception as e:
#         # Если произошла ошибка, откатываем транзакцию
#         db_session_after_close.rollback()  # откат всех введеных нами изменений
#         pytest.fail(f"Ошибка при переводе денег: {e}")
#
#     finally:
#         # Удаляем данные для тестирования из базы
#         db_session_after_close.delete(stan)
#         db_session_after_close.delete(bob)
#         # Фиксируем изменения в базе данных
#         db_session_after_close.commit()


# def test_delite_movie(api_manager, super_admin_token, db_session_after_close):
#
#     movie = DataGenerator.generate_random_movie()
#     response = api_manager.movies_api.create_movie(movie_data=movie, token=super_admin_token)
#     id_movie = api_manager.movies_api.info_id(response)
#
#     search_movie = db_session_after_close.query(MovieDBModel).filter(MovieDBModel.id == id_movie)
#     assert search_movie.count() == 1
#
#     #delete_response = api_manager.movies_api.delete_movie(movie_id=id_movie, token=super_admin_token, expected_status=200)
#
#     get_response = api_manager.movies_api.get_movie_by_id(id_movie, expected_status=(200, 404))
#     if get_response.status_code != 404:
#         x = (
#             delete(MovieDBModel)
#             .where(MovieDBModel.id == id_movie)
#             .returning(MovieDBModel.id)
#         )
#         db_session_after_close.execute(x).scalar_one_or_none()
#         db_session_after_close.commit()


import allure
import random
from module_5.Cinescope.db_requester.models import AccountTransactionTemplate
import pytest
from module_5.Cinescope.conftest import db_session_after_close
# Оригинал теста, без allure в module_5/Cinescope/tests/api/test_other_api.py

@allure.epic("Тестирование транзакций")
@allure.feature("Тестирование транзакций между счетами")
class TestAccountTransactionTemplate:

    @allure.story("Корректность перевода денег между двумя счетами")
    @allure.description("""
        Этот тест проверяет корректность перевода денег между двумя счетами.
        Шаги:
        1. Создание двух счетов: Stan и Bob.
        2. Перевод 200 единиц от Stan к Bob.
        3. Проверка изменения балансов.
        4. Очистка тестовых данных.
        """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("qa_name", "Ivan Petrovich")
    @allure.title("Тест перевода денег между счетами 200 рублей")

    def test_accounts_transaction_template(self, db_session_after_close: "Session"):
        # ====================================================================== Подготовка к тесту
        with allure.step("Создание тестовых данных в базе данных: счета Stan и Bob (чтоб точно быть уверенными, что в базе присутствуют данные для тестирования)"):
            stan = AccountTransactionTemplate(user=f"Stas_{random.randint(1000, 10000)}", balance=1000)
            bob = AccountTransactionTemplate(user=f"Bober_{random.randint(1000, 10000)}", balance=500)

            # Добавляем записи в сессию
            db_session_after_close.add_all([stan, bob])
            # Фиксируем изменения в базе данных
            db_session_after_close.commit()

        @allure.step("Функция перевода денег: transfer_money")
        @allure.description("""
                    функция выполняющая транзакцию, имитация вызова функции на стороне тестируемого сервиса
                    и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
                    """)

        def transfer_money(session, from_account, to_account, amount):

            """
            Переводит деньги с одного счета на другой.
            :param session: Сессия SQLAlchemy.
            :param from_account_id: ID счета, с которого списываются деньги.
            :param to_account_id: ID счета, на который зачисляются деньги.
            :param amount: Сумма перевода.
            """
            with allure.step(" Получаем счета"):
                from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
                to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

            with allure.step("Проверяем, что на счете достаточно средств"):
                if from_account.balance < amount:
                    raise ValueError("Недостаточно средств на счете")

            with allure.step("Выполняем перевод"):
                from_account.balance -= amount
                to_account.balance += amount

            with allure.step("Сохраняем изменения"):
                session.commit()

        # ====================================================================== Тест
        with allure.step("Проверяем начальные балансы"):
            assert stan.balance == 1000
            assert bob.balance == 500

        try:
            with allure.step("Выполняем перевод 200 единиц от stan к bob"):
                transfer_money(db_session_after_close, from_account=stan.user, to_account=bob.user, amount=200)

            with allure.step("Проверяем, что балансы изменились"):
                assert stan.balance == 800
                assert bob.balance == 700

        except Exception as e:
            with allure.step("ОШИБКА, откаты транзакции"):
            # Если произошла ошибка, откатываем транзакцию
                db_session_after_close.rollback()  # откат всех введеных нами изменений
            pytest.fail(f"Ошибка при переводе денег: {e}")

        finally:
            with allure.step("Удаляем данные для тестирования из базы"):
                db_session_after_close.delete(stan)
                db_session_after_close.delete(bob)
                # Фиксируем изменения в базе данных
                db_session_after_close.commit()

