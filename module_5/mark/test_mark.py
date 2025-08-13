import pytest

@pytest.mark.skip(reason='Не будем тестировать')
def test_something_test():
    print('its not printed')

skip_test = True
@pytest.mark.skipif(skip_test, reason="Тест отключён вручную")
def test_skipif_demo():
    assert True


@pytest.mark.skipif(reason='off')
def test_admin_creation_logs_mark(admin_user): #если отключить скип, тест не найдет фикстуру в каталоге, работать не будет
    assert True


import pytest
import sys

@pytest.mark.skipif(
    sys.platform != "linux",
    reason="Тест только для Linux"
)
def test_linux_only():
    assert True

@pytest.mark.skipif(
    sys.platform != "darwin",
    reason="Тест только для mac"
)
def test_mac_only():
    assert True


import os

@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Не запускать в CI"
)
def test_local_only():
    assert os.getenv("CI") != "true"

@pytest.mark.xfail(reason='Ожидаемо упадет')
def test_func():
   assert 2 + 2 == 5

@pytest.mark.xfail(reason='Ожидаемо не упадет')
def test_func1():
    assert 2 + 2 == 4


@pytest.fixture
def my_fixture():
    print('its fixture')

@pytest.mark.usefixtures("my_fixture")
def test_func2():
    print(' its not fixture')

@pytest.fixture
def my_fixture1():
    print('its fixture')

def test_func3(my_fixture1):
    print(' its not fixture')