from module_5.Cinescope.custom_requester.custom_requester import CustomRequester
from module_5.Cinescope.constants import BASE_URL

class UserAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """

    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL) #base_url=session.base_url
        # self.session = session

    def get_user_info(self, user_id, expected_status=200):
        """
        Получение информации о пользователе.
        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="GET",
            endpoint=f"/user/{user_id}",
            expected_status=expected_status
        )

    def delete_user(self, user_id, expected_status=204):
        """
        Удаление пользователя.
        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="DELETE",
            endpoint=f"/user/{user_id}",
            expected_status=expected_status
        )

    def get_user(self, user_locator, expected_status=200): # user_locator - email or id
        return self.send_request(
            "GET",
            f"/user/{user_locator}",
            expected_status=expected_status)

    def create_user(self, user_data, expected_status=201):
        return self.send_request(
            method="POST",
            endpoint="/user/",
            data=user_data,
            expected_status=expected_status
        )

    def change_role_to_admin(self, user_id: str, expected_status=200):
        body = {
            "roles": ["USER", "ADMIN"],
            "verified": True,
            "banned": False
        }
        return self.send_request(
            method="PATCH",
            endpoint=f"/user/{user_id}",
            data=body,
            expected_status=expected_status
        )