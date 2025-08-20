from module_5.Cinescope.models.base_models import TestUser, RegisterUserResponse, ErrorResponse


class TestsUser:

    # def test_create_user(self, super_admin, creation_user_data):
    #
    #     response = super_admin.api.user_api.create_user(creation_user_data).json()
    #
    #     assert response.get('id') and response['id'] != '', "ID должен быть не пустым"
    #     assert response.get('email') == creation_user_data['email']
    #     assert response.get('fullName') == creation_user_data['fullName']
    #     assert response.get('roles', []) == creation_user_data['roles']
    #     assert response.get('verified') is True

    def test_create_user(self, super_admin, creation_user_data):

        TestUser(**creation_user_data)
        response = super_admin.api.user_api.create_user(creation_user_data).json()
        RegisterUserResponse(**response)

    # def test_get_user_by_locator(self, super_admin, creation_user_data):
    #     created_user_response = super_admin.api.user_api.create_user(creation_user_data).json()
    #     response_by_id = super_admin.api.user_api.get_user(created_user_response['id']).json()
    #     response_by_email = super_admin.api.user_api.get_user(creation_user_data['email']).json()
    #
    #     assert response_by_id == response_by_email, "Содержание ответов должно быть идентичным"
    #     assert response_by_id.get('id') and response_by_id['id'] != '', "ID должен быть не пустым"
    #     assert response_by_id.get('email') == creation_user_data['email']
    #     assert response_by_id.get('fullName') == creation_user_data['fullName']
    #     assert response_by_id.get('roles', []) == creation_user_data['roles']
    #     assert response_by_id.get('verified') is True

    def test_get_user_by_locator(self, super_admin, creation_user_data):
        test_data = TestUser(**creation_user_data) #Валидируем модель запроса

        # Создаем пользователя, убрали .json()
        response_create = super_admin.api.user_api.create_user(test_data.model_dump(mode="json", exclude_unset=True))
        assert response_create.status_code == 201, response_create.text
        created = RegisterUserResponse(**response_create.json())

        #Получаем пользователя по id
        response_by_id = super_admin.api.user_api.get_user(created.id)
        assert response_by_id.status_code == 200, response_by_id.text
        by_id = RegisterUserResponse(**response_by_id.json())

        # Получаем пользователя по email
        response_by_email = super_admin.api.user_api.get_user(created.email)
        assert response_by_email.status_code == 200, response_by_email.text
        by_email = RegisterUserResponse(**response_by_email.json())

        # Сверяем ответы между собой
        assert by_id.id == by_email.id, "ID должны совпадать"
        assert by_id.email == by_email.email, "Email должен совпадать"
        assert by_id.fullName == by_email.fullName, "fullName должен совпадать"
        assert set(by_id.roles) == set(by_email.roles), "Роли должны совпадать"
        assert by_id.verified == by_email.verified, "verified должен совпадать"
        assert by_id.banned == by_email.banned, "banned должен совпадать"

        # И с исходными данными создания
        assert by_id.email == test_data.email
        assert by_id.fullName == test_data.fullName
        assert set(by_id.roles) == set(test_data.roles)  # если роли задаются при создании
        assert by_id.verified is True

    # def test_get_user_by_id_common_user(self, common_user):
    #     common_user.api.user_api.get_user(common_user.email, expected_status=403)

    def test_get_user_by_id_common_user(self, common_user):

        response = common_user.api.user_api.get_user(common_user.email, expected_status=403)
        error_response = ErrorResponse(**response.json())

        assert response.status_code == 403
        assert error_response.statusCode == 403
        assert isinstance(error_response.message, str) and error_response.message
