'''
pytest                    # запуск всех тестов
pytest --durations=5      # показать 5 самых медленных тестов
pytest --setup-plan       # порядок выполнения setup/teardown
pytest --fixtures         # список доступных фикстур
pytest --markers          # список зарегистрированных маркеров
pytest --co               # структура тестов без запуска
pytest test_user_api.py   # запуск одного файла
pytest -v                 # подробный вывод
pytest -q                 # краткий режим
pytest -x                 # остановка на первом упавшем тесте
pytest -k create_user     # запуск по имени (подстрока)
pytest -m slow            # запуск всех тестов, где марка slow
'''

'''Встроенные метки'''

import pytest

@pytest.mark.skip(reason="Временно отключён")
def test_example():
    assert 1 + 1 == 2


skip_test = True
@pytest.mark.skipif(skip_test, reason="Тест отключён вручную")
def test_skipif_demo():
    assert True


@pytest.mark.xfail(reason="Функция ещё не реализована")
def test_future_feature():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг в системе")
def test_fixed_bug():
    assert 2 + 2 == 4



@pytest.fixture
def setup_data():
    print("Setup_111")

@pytest.mark.usefixtures("setup_data") #Используем фикстуру, через маркер
def test_with_usefixtures():
    assert True


@pytest.fixture
def setup_data1():
    print("Setup_222")

def test_with_fixture(setup_data1): #Используем фикстуру, в аргументе
    assert True

'''Кастомные метки'''

import pytest

@pytest.mark.smoke
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.api
def test_multiplication():
    assert 2 * 3 == 6

@pytest.mark.slow
def test_division():
    assert 10 / 2 == 5

@pytest.mark.db
def test_mark_db():
    assert 1 + 1 == 2

@pytest.mark.ui
def test_mark_ui():
    assert 2 + 2 == 4

@pytest.mark.ui1
def test_mark_ui():
    assert 2 + 2 == 4

'''Метки в реальных тестах'''

import pytest
import time

@pytest.mark.smoke
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.smoke
def test_multiplication():
    assert 2 * 3 == 6

@pytest.mark.slow
def test_division():
    assert 10 / 2 == 5

@pytest.mark.api
@pytest.mark.slow
def test_string_concatenation():
    time.sleep(5)
    assert "Hello " + "World" == "Hello World"

@pytest.mark.api
def test_string_upper():
    assert "hello".upper() == "HELLO"

@pytest.mark.smoke
@pytest.mark.api
def test_list_append():
    lst = [1, 2, 3]
    lst.append(4)
    assert lst == [1, 2, 3, 4]

@pytest.mark.skip(reason="Временно отключен")
def test_list_remove():
    lst = [1, 2, 3, 4]
    lst.remove(3)
    assert lst == [1, 2, 4]

@pytest.mark.healthcheck
def test_dict_get():
    d = {'key': 'value'}
    assert d.get('key') == 'value'

@pytest.mark.regression
@pytest.mark.integration
def test_dict_set():
    d = {}
    d['key'] = 'value'
    assert d['key'] == 'value'

@pytest.mark.flaky
def test_random_fail():
    import random
    assert random.choice([True, False])


import pytest
@pytest.mark.flaky
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_maybe_fails():
    import random
    assert random.choice([True, False])


