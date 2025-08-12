import pytest
from module_5.Cinescope.resources.user_creds import SuperAdminCreds


@pytest.mark.parametrize("email, password, expected_status", [
    (f"{SuperAdminCreds.USERNAME}", f"{SuperAdminCreds.PASSWORD}", 200),
    ("test_login1@email.com", "asdqwe123Q!", 401),  # Сервис не может обработать логин по незареганному юзеру
    ("", "password", 401),
], ids=["Admin login", "Invalid user", "Empty username"])
def test_login(email, password, expected_status, api_manager):
    login_data = {
        "email": email,
        "password": password
    }
    api_manager.auth_api.login_user(login_data=login_data, expected_status=expected_status)

# locations_choice = ['MSK', 'SPB']
#     created_at_choice = ['asc', 'desc']
#     # boolean_choice = ['true', 'false']
#
#     pageSize = random.randint(1, 20)
#     page = random.randint(1, 5) #всего 2029 фильма
#     min_price = random.randint(1, 1000)
#     max_price = random.randint(1, 10000)
#     locations = random.choice(locations_choice)
#     published = str(faker.boolean()).lower()    #(random.choice(boolean_choice))
#     genreId = random.randint(1, 10)
#     createdAt = random.choice(created_at_choice)
#
#     params =  {
#         "pageSize": pageSize,
#         "page": page,
#         "min_price": min_price,
#         "max_price": max_price,
#         "locations": locations,
#         "published": published,
#         "genreId": genreId,
#         "createdAt": createdAt
#     }
#
#     return params


@pytest.mark.parametrize("min_price,max_price,locations,genreId", [
    (1, 1000, 'MSK', 1),
    (1, 1000, 'SPB', 5),
    (1, 1000, 'SPB', 7),
], ids=['1 test', '2 test', '3 test'])
def test_get_movies_filter_params(api_manager, min_price, max_price, locations, genreId):
    params = {
              "min_price": min_price,
              "max_price": max_price,
              "locations": locations,
              "genreId": genreId
              }
    response = api_manager.movies_api.get_all_movies(**params).json()

    assert "movies" in response, "В ответе нет 'movies'"
    assert isinstance(response["movies"], list), "movies должен быть списком"

    for movie in response["movies"]:

        if "genreId" in params and params['genreId'] is not None:
            assert "genreId" in movie, '"genreId" нет в movie'
            assert movie["genreId"] == params["genreId"], '"genreId" в выдаче, не соответствует заданному'

        if "locations" in params and params['locations'] is not None:
            assert "location" in movie, '"location" нет в movie'
            assert movie["location"] == params["locations"], '"locations" в выдаче, не соответствует заданному'

        if "max_price" in params:
            assert movie['price'] <= params['max_price'], 'max price в выдаче, больше заданной по условию '

        if "min_price" in params:
            assert movie['price'] >= params['min_price'], 'min price в выдаче, меньше заданной по условию '