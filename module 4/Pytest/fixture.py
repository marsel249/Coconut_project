# import pytest
#
# @pytest.fixture
# def input_data():
#     return [1, 2, 3, 4, 5]
'''Фикстура перенесена в conftest.py'''

def test_sum(input_data): #используем фикстуру как аргумент функции
    assert sum(input_data) == 15

def test_len(input_data): #используем фикстуру как аргумент функции
    assert len(input_data) == 5

# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="session")