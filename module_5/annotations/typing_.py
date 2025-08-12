from typing import Union, List, Optional, Dict, Tuple, Set

def add(a: int, b: int) -> int:
    return a + b

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def process_input(value: Union[int, str]) -> str:
    return f"Ты передал: {value}"

def user_info() -> Dict[str, int]:
    return {"age": 25, "height": 180}

def get_coordinates() -> Tuple[float, float]:
    return (55.7558, 37.6173)  # Москва: широта, долгота

def unique_numbers(numbers: Set[int]) -> Set[int]:
    return set(numbers)

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Привет, меня зовут {self.name}!"

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Пользователь найден"
    return None


