import random

from module_5.Cinescope.api.api_manager import ApiManager
from module_5.Cinescope.utils.data_generator import DataGenerator

class TestPatchMoviesAPI:

    def test_patch_movie(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie'''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)
        response = api_manager.movies_api.update_movie(id, patch_movie_data)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() != first_response.json(), "Данные фильма изменились"

    # def test_patch_movie_double(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):
    #
    #     '''Попытка сделать копию фильма. Создаем фильм, патчим его генерируемыми данными, создаем фильм,
    #     пытаемся пропатчить его теми же данными'''
    #
    #     patch_movie = patch_movie_data.copy()
    #
    #     id = api_manager.movies_api.info_id(create_movie)
    #     first_response = api_manager.movies_api.get_movie_by_id(id)
    #     response = api_manager.movies_api.update_movie(id, patch_movie) #Создали фильм, пропатчили его
    #     get_movie = api_manager.movies_api.get_movie_by_id(id).json()
    #
    #     movie_data = DataGenerator.generate_random_movie()
    #     create_second_movie = api_manager.movies_api.create_movie(movie_data, expected_status=201)
    #     id_2 = api_manager.movies_api.info_id(create_second_movie) #узнали id нового фильма
    #     get_second_movie = api_manager.movies_api.get_movie_by_id(id_2) #Получили дату нового фильма
    #     response = api_manager.movies_api.update_movie(id_2, patch_movie, expected_status=400) #Патчим второй фильм той же датой
    #     get_second_movie_2 = api_manager.movies_api.get_movie_by_id(id_2).json()
    #
    #     assert get_second_movie_2 != get_movie
    #     # assert response.status_code == 400



    def test_patch_price(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, price = float, бэк округляет price '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['price'] = round(random.uniform(1,100), 2)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=200)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() != first_response.json(), "Данные фильма изменились"


    def test_NEGATIVE_patch_movie_empty_data(self, api_manager: ApiManager, super_admin_auth, create_movie):

        '''NEGATIVE patch movie, empty data'''

        data = {}
        id_movie = create_movie.json()['id']
        before_response = api_manager.movies_api.get_movie_by_id(id_movie)
        response = api_manager.movies_api.update_movie(id_movie, data)
        after_response = api_manager.movies_api.get_movie_by_id(id_movie)

        assert before_response.json() == after_response.json()
        assert response.status_code == 200

    def test_NEGATIVE_patch_movie_without_auth(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, without auth'''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        del_auth = api_manager.auth_api.del_auth()

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=401)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_name_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, name = '' '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['name'] = ''

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_name_2(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, name = 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['name'] = 0

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_name_3(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, name = число '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['name'] = random.randint(-100, 100)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"


    def test_NEGATIVE_patch_price_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, price = '' '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['price'] = ''

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_price_2(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, price = 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['price'] = 0

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_price_3(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, price < 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['price'] = random.randint(-100, -1)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_price_4(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, price = str'''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['price'] = DataGenerator.generate_random_word()

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_description_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, description - число '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['description'] = random.randint(-100, 100)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_location_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, location - число '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['location'] = random.randint(-100, 100)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_location_2(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, location - random.word '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['location'] = DataGenerator.generate_random_city()

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_location_3(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, location - 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['location'] = 0

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_imageUrl_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, imageUrl - 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['imageUrl'] = 0

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_imageUrl_2(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, imageUrl - число '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['imageUrl'] = random.randint(-100, 100)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_imageUrl_3(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, imageUrl - random.word '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['imageUrl'] = DataGenerator.generate_random_city()

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_genreId_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, genreId - 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['genreId'] = 0

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"


    def test_NEGATIVE_patch_genreId_2(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, genreId < 0 '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['genreId'] = random.randint(-100, -1)

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"

    def test_NEGATIVE_patch_published_1(self, api_manager: ApiManager, super_admin_auth, create_movie, patch_movie_data):

        '''patch movie, published nat a bool '''

        id = api_manager.movies_api.info_id(create_movie)
        first_response = api_manager.movies_api.get_movie_by_id(id)

        patch_movie_data['published'] = 'notabool'

        response = api_manager.movies_api.update_movie(id, patch_movie_data, expected_status=400)
        response = api_manager.movies_api.get_movie_by_id(id)
        assert response.json() == first_response.json(), "Данные фильма не изменились"
