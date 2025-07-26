from module_4.Cinescope.custom_requester.custom_requester import CustomRequester
from module_4.Cinescope.constants import CINESCOPE_URL


class MoviesAPI(CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url=CINESCOPE_URL)

    def get_all_movies(self, page=1, page_size=10, min_price=None, max_price=None,
                       locations=None, published=None, sort=None, expected_status=200):
        """
        Получить список фильмов с пагинацией и фильтрами

        page: номер страницы (по умолчанию 1)
        page_size: количество на странице (по умолчанию 10)
        min_price: минимальная цена
        max_price: максимальная цена
        locations: города через запятую (например "MSK,SPB")
        published: только опубликованные (True/False)
        sort: сортировка (например "createdAt:asc")
        expected_status: ожидаемый статус ответа
        """
        params = {
            "page": page,
            "pageSize": page_size
        }

        if min_price is not None:
            params["minPrice"] = min_price
        if max_price is not None:
            params["maxPrice"] = max_price
        if locations:
            params["locations"] = locations
        if published is not None:
            params["published"] = str(published).lower()
        if sort:
            params["sort"] = sort

        return self.send_request(
            method="GET",
            endpoint="/movie",
            params=params,
            expected_status=expected_status
        )

    def get_movie_by_id(self, movie_id, expected_status=200):
        """Получить фильм по ID"""
        return self.send_request(
            method="GET",
            endpoint=f"/movie/{movie_id}",
            expected_status=expected_status
        )

    def create_movie(self, movie_data, expected_status=201):
        """Создать новый фильм"""
        return self.send_request(
            method="POST",
            endpoint="/movie",
            data=movie_data,
            expected_status=expected_status
        )

    def update_movie(self, movie_id, update_data, expected_status=200):
        """Обновить данные фильма"""
        return self.send_request(
            method="PATCH",
            endpoint=f"/movie/{movie_id}",
            data=update_data,
            expected_status=expected_status
        )

    def delete_movie(self, movie_id, expected_status=204):
        """Удалить фильм"""
        return self.send_request(
            method="DELETE",
            endpoint=f"/movie/{movie_id}",
            expected_status=expected_status
        )