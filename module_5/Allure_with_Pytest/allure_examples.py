import allure  # Импортируем пакет allure
import pytest


# @allure.title("Проверка сложения двух чисел")
# @allure.description("Тест проверяет, что сумма двух чисел вычисляется корректно")
# def test_addition():
#     with allure.step("Проверка суммы 2 + 2"):
#         assert 2 + 2 == 4
#
#     with allure.step("Проверка суммы 3 + 2"):
#         assert 2 + 2 == 5



# @allure.title("Проверка сложения чисел {a} и {b}")
# @allure.description('Тут мы проверяем сложение чисел')
# @pytest.mark.parametrize("a,b,expected", [
#     (2, 4, 6),
#     (4, 4, 8)
# ])
# def test_addition(a, b, expected):
#     with allure.step('Проверка суммы:'):
#         assert a + b == expected
#     with allure.step('Проверка вычитания expected - a = b'):
#         assert expected - a == b



# #Также декоратор @allure.step можно применить на вызываемые из тестов функции
# # что позволит использовать ее в разных тестах, но продолжать генерировать красивые отчеты
# @allure.step("Проверка сложения чисел {a} и {b}")
# def check_addition(a, b, expected):
#     with allure.step(f"Сложение {a} и {b}"):
#         result = a + b
#     with allure.step(f"Проверка результата {result} == {expected}"):
#         assert result == expected
#
# def test_addition():
#     check_addition(2, 2, 4)
#     check_addition(3, 5, 8)
#
# @allure.epic("Cinescop")
# @allure.feature("movie_api")
# @allure.story("video_generator")
# def test_generate_video():
#     assert 1 + 1 == 2
#
# @allure.tag("smoke", "regression")
# def test_smoke_feature():
#     assert 1 + 1 == 2
#
# @allure.link("https://jira.com/task/QA_TEAM_322", name="Очень важный баг")
# def test_with_link():
#     assert 1 + 1 == 2
#
# @allure.label("owner", "team-qa")
# @allure.label("qa_name", "Ivan Petrovich")
# def test_with_custom_labels():
#     assert 1 + 1 == 2
#
# def test_with_attachment():
#     allure.attach("Текстовые данные", name="log.txt", attachment_type=allure.attachment_type.TEXT)
#     allure.attach.file("./screenshot.png", name="Скриншот", attachment_type=allure.attachment_type.PNG)



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

# Тест теперь генирируется в этой директории
# @allure.epic("Тестирование транзакций") - Главная папка
# @allure.feature("Тестирование транзакций между счетами") - подпапка
# @allure.story("Корректность перевода денег между двумя счетами")  - подпапка
# @allure.title("Тест перевода денег между счетами 200 рублей")  - название теста с отчетом

# Описание, которое тянется в Allure
#     @allure.description("""
#     Этот тест проверяет корректность перевода денег между двумя счетами.
#     Шаги:
#     1. Создание двух счетов: Stan и Bob.
#     2. Перевод 200 единиц от Stan к Bob.
#     3. Проверка изменения балансов.
#     4. Очистка тестовых данных.
#     """)

# - У теста есть владелец “@allure.label("qa_name", "Ivan Petrovich")”
# - А также мы указали уровень важности данного кейса “@allure.severity(allure.severity_level.CRITICAL)”

