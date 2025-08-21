import random
import string
from faker import Faker
from uuid import uuid4
from datetime import datetime, timezone

faker = Faker()


class DataGenerator:

    # @staticmethod
    # def generate_random_email():
    #     random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    #     return f"kek{random_string}@gmail.com"

    @staticmethod
    def generate_random_email() -> str:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
        return f"autotest{ts}{uuid4().hex[:6]}@gmail.com"


    @staticmethod
    def generate_random_name():
        return f"{faker.first_name()} {faker.last_name()}"


    @staticmethod
    def generate_random_password():
        """
        Генерация пароля, соответствующего требованиям:
        - Минимум 1 буква.
        - Минимум 1 цифра.
        - Допустимые символы.
        - Длина от 8 до 20 символов.
        """
        # Гарантируем наличие хотя бы одной буквы и одной цифры
        letters = random.choice(string.ascii_letters)  # Одна буква
        digits = random.choice(string.digits)  # Одна цифра

        # Дополняем пароль случайными символами из допустимого набора
        special_chars = "?@#$%^&*|:"
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining_length = random.randint(6, 18)  # Остальная длина пароля
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return ''.join(password)

    @staticmethod
    def generate_random_movie():
        locations_choice = ['MSK', 'SPB']
        # boolean_choice = ['true', 'false']

        movie_data = {
            "name": " ".join(faker.words(2)), #faker.word(),
            "imageUrl": faker.url(),
            "price": random.randint(1, 10000),
            "description": faker.text(),
            "location": random.choice(locations_choice),
            "published": bool(str(faker.boolean()).lower()),  # random.choice(boolean_choice)
            "genreId": random.randint(1, 5)
        }

        return movie_data

    @staticmethod
    def generate_random_string(length):
        return ''.join(faker.random_letters(length))

    @staticmethod
    def generate_random_city():
        return faker.city()

    @staticmethod
    def generate_random_word():
        return faker.word()

    @staticmethod
    def generate_random_user_id() -> str:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
        return f"random_id_{ts}{uuid4().hex[:5]}"

