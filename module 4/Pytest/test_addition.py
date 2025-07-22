# test_addition.py

def test_addition():
    assert 2 + 2 == 4

def test_additio():
    assert 2 - 2 == 4

def test_string_contains():
    text = "hello world"
    substring = "world"
    assert substring in text, f"Подстрока '{substring}' не найдена в строке '{text}'"

