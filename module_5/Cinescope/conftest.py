#booker
import random

from faker import Faker
import pytest
import requests
from module_5.Cinescope.constants import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT, SUPER_ADMIN_CREDS
from module_5.Cinescope.custom_requester.custom_requester import CustomRequester
from module_5.Cinescope.utils.data_generator import DataGenerator
from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.resources.user_creds import SuperAdminCreds
from module_5.Cinescope.entities.user import User
from module_5.Cinescope.enums.enums import Roles
from module_5.Cinescope.models.base_models import TestUser
from enum import Enum

faker = Faker()

'''
Фикстура до рефакторинга

@pytest.fixture(scope="session")
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": Roles.USER.value
    }'''

@pytest.fixture
def test_user() -> TestUser:
    random_password = DataGenerator.generate_random_password()

    return TestUser(
        email=DataGenerator.generate_random_email(),
        fullName=DataGenerator.generate_random_name(),
        password=random_password,
        passwordRepeat=random_password,
        roles=[Roles.USER]#[Roles.USER.value]
    )

@pytest.fixture
def registration_user_data() -> TestUser:
    random_password = DataGenerator.generate_random_password()

    return TestUser(
        email=DataGenerator.generate_random_email(),
        fullName=DataGenerator.generate_random_name(),
        password=random_password,
        passwordRepeat=random_password,
        roles=[Roles.USER]#[Roles.USER.value]
    )

@pytest.fixture()#scope="session")
def registered_user(requester, test_user):
    """
    Фикстура для регистрации и получения данных зарегистрированного пользователя.
    """
    response = requester.send_request(
        method="POST",
        endpoint=REGISTER_ENDPOINT,
        data=test_user,
        expected_status=201
    )
    response_data = response.json()
    registered_user = test_user.copy()
    registered_user["id"] = response_data["id"]
    return registered_user




@pytest.fixture(scope="session")
def requester():
    """
    Фикстура создаёт экземпляр CustomRequester с базовыми настройками
    """
    session = requests.Session()
    return CustomRequester(session=session, base_url=BASE_URL)

@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    Создаёт HTTP-сессию (общую для всех тестов)
    Устанавливает базовый URL
    """
    http_session = requests.Session()
    http_session.base_url = BASE_URL
    yield http_session
    http_session.close()

@pytest.fixture(scope="session")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager
    Инициализирует ApiManager с общей сессией. Предоставляет единую точку доступа ко всем API
    """
    return ApiManager(session)

@pytest.fixture()
def super_admin_auth(api_manager):
    '''авторизация супер админа'''
    response = api_manager.auth_api.authenticate(SUPER_ADMIN_CREDS)
    return response

@pytest.fixture()
def create_movie(api_manager):

    locations_choice = ['MSK', 'SPB']
    # boolean_choice = ['true', 'false']

    movie_data = {
  "name": " ".join(faker.words(2)), #faker.word(),
  "imageUrl": faker.url(),
  "price": random.randint(1, 10000),
  "description": faker.text(),
  "location": random.choice(locations_choice),
  "published": bool(str(faker.boolean()).lower()), #random.choice(boolean_choice)
  "genreId": random.randint(1, 5)
}
    """Создать новый фильм"""
    response = api_manager.movies_api.create_movie(movie_data)
    return response

@pytest.fixture()
def filter_params():
    #Значения пока оставил рандомные

    locations_choice = ['MSK', 'SPB']
    created_at_choice = ['asc', 'desc']
    # boolean_choice = ['true', 'false']

    pageSize = random.randint(1, 20)
    page = random.randint(1, 5) #всего 2029 фильма
    min_price = random.randint(1, 1000)
    max_price = random.randint(1, 10000)
    locations = random.choice(locations_choice)
    published = str(faker.boolean()).lower()    #(random.choice(boolean_choice))
    genreId = random.randint(1, 10)
    createdAt = random.choice(created_at_choice)

    params =  {
        "pageSize": pageSize,
        "page": page,
        "min_price": min_price,
        "max_price": max_price,
        "locations": locations,
        "published": published,
        "genreId": genreId,
        "createdAt": createdAt
    }

    return params

@pytest.fixture()
def patch_movie_data():
    locations_choice = ['MSK', 'SPB']

    movie_data = {
        "name": faker.word(),
        "imageUrl": faker.url(),
        "price": random.randint(1, 10000),
        "description": faker.text(),
        "location": random.choice(locations_choice),
        "published": bool(str(faker.boolean()).lower()),
        "genreId": random.randint(1, 5)
    }

    new_movie_data = {}
    items = list(movie_data.items())
    random.shuffle(items)
    num_items = random.randint(1, len(items))
    for key, value in items[:num_items]:
        new_movie_data[key] = value

    return new_movie_data

@pytest.fixture
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = ApiManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()

'''
До рефакторинга
@pytest.fixture(scope="function")
def creation_user_data(test_user):
    updated_data = test_user.copy()
    updated_data.update({
        "verified": True, "banned": False
    })
    return updated_data'''

@pytest.fixture(scope="function")
def creation_user_data(test_user: TestUser) -> dict:
    payload = test_user.model_dump()  # Преобразовали модель test_user  в словарь
    payload["verified"] = True
    payload["banned"] = False

    # Заодно гарантия: конвертируем Enum -> value, если вдруг что-то проскочило
    # payload["roles"] = [
    #     r.value if isinstance(r, Enum) else r
    #     for r in payload.get("roles", [])
    # ]

    out = []
    for r in payload.get("roles", []):
        if isinstance(r, Enum):
            out.append(r.value)
        else:
            out.append(r)
    payload["roles"] = out

    # Быстрая самопроверка перед отправкой
    assert isinstance(payload["roles"], list)
    assert all(isinstance(x, str) for x in payload["roles"])

    return payload


@pytest.fixture
def super_admin(user_session):
    new_session = user_session()

    super_admin = User(
        SuperAdminCreds.USERNAME,
        SuperAdminCreds.PASSWORD,
        Roles.SUPER_ADMIN.value,
        new_session)

    super_admin.api.auth_api.authenticate(super_admin.creds)
    return super_admin

@pytest.fixture
def common_user(user_session, super_admin, creation_user_data):
    new_session = user_session()

    common_user = User(
        creation_user_data['email'],
        creation_user_data['password'],
        Roles.USER.value,
        new_session)

    super_admin.api.user_api.create_user(creation_user_data)
    common_user.api.auth_api.authenticate(common_user.creds)
    return common_user


@pytest.fixture
def admin_user(user_session, super_admin, creation_user_data):
    session = user_session()

    payload = dict(creation_user_data)
    payload.setdefault("passwordRepeat", payload["password"])
    payload.setdefault("verified", True)
    payload.setdefault("banned", False)

    create_resp = super_admin.api.user_api.create_user(payload, expected_status=201).json()
    user_id = create_resp["id"]

    super_admin.api.user_api.change_role_to_admin(user_id, expected_status=200)

    admin = User(payload["email"],
                 payload["password"],
                 Roles.ADMIN.value,
                 session)

    admin.api.auth_api.authenticate(admin.creds)

    return admin





