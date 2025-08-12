import pytest
from module_5.Cinescope.resources.user_creds import SuperAdminCreds


@pytest.mark.parametrize("email, password, expected_status", [
    (f"{SuperAdminCreds.USERNAME}", f"{SuperAdminCreds.PASSWORD}", (200, 201)),
    ("test_login1@email.com", "asdqwe123Q!", 500),  # Сервис не может обработать логин по незареганному юзеру
    ("", "password", 500),
], ids=["Admin login", "Invalid user", "Empty username"])
def test_login(email, password, expected_status, api_manager):
    login_data = {
        "email": email,
        "password": password
    }
    api_manager.auth_api.login_user(login_data=login_data, expected_status=expected_status)