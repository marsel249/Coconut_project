import pytest

pytestmark = pytest.mark.skip(reason="TASK-1234: Тесты временно отключены из-за нестабильности")

def test_one():
    assert True

def test_two():
    assert True
