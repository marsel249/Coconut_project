from module_5.Cinescope.custom_requester.custom_requester import CustomRequester
from module_5.Cinescope.constants import CINESCOPE_URL


class MoviesAPI(CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url=CINESCOPE_URL)

    def get_all_movies(self, pageSize=None, page=None, min_price=None, max_price=None,
                       locations=None, published=None, genreId=None, sort=None, createdAt=None, expected_status=200):
        """
        Получить список фильмов с пагинацией и фильтрами"""

        params = {}

        if pageSize is not None:
            params["pageSize"] = pageSize
        if page is not None:
            params["page"] = page
        if min_price is not None:
            params["minPrice"] = min_price
        if max_price is not None:
            params["maxPrice"] = max_price
        if locations is not None:
            params["locations"] = locations
        if published is not None:
            params["published"] = published
        if genreId is not None:
            params['genreId'] = genreId
        if sort is not None:
            params["sort"] = sort
        if createdAt is not None:
            params["createdAt"] = createdAt

        return self.send_request(
            method="GET",
            endpoint="/movies",
            params=params,
            expected_status=expected_status
        )

    def get_movie_by_id(self, movie_id, expected_status=200):
        """Получить фильм по ID"""
        return self.send_request(
            method="GET",
            endpoint=f"/movies/{movie_id}",
            expected_status=expected_status
        )

    def create_movie(self, movie_data, expected_status=201, token=None):
        """Создать новый фильм"""
        return self.send_request(
            method="POST",
            endpoint="/movies",
            data=movie_data,
            expected_status=expected_status,
            token=token
        )

    def update_movie(self, movie_id, update_data, expected_status=200, token=None):
        """Обновить данные фильма"""
        return self.send_request(
            method="PATCH",
            endpoint=f"/movies/{movie_id}",
            data=update_data,
            expected_status=expected_status,
            token=token
        )

    def delete_movie(self, movie_id, expected_status=204, token=None):
        """Удалить фильм"""
        return self.send_request(
            method="DELETE",
            endpoint=f"/movies/{movie_id}",
            expected_status=expected_status,
            token=token
        )

    def info_id(self, variable):
        x = variable.json()
        return x['id']

