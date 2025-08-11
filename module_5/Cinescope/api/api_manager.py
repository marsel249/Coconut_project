from module_5.Cinescope.api.auth_api import AuthAPI
from module_5.Cinescope.api.user_api import UserAPI
from module_5.Cinescope.api.movies_api import MoviesAPI

class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):
        """
        Инициализация ApiManager.
        :param session: HTTP-сессия, используемая всеми API-классами.
        """
        self.session = session
        self.auth_api = AuthAPI(session)
        self.user_api = UserAPI(session)
        self.movies_api = MoviesAPI(session)

    def close_session(self):
        self.session.close()
'''
    Pytest->>TestFile: Запуск теста test_register_user()
    TestFile->>Conftest: Запрос фикстур (api_manager, test_user)
    Conftest->>Conftest: Создает session → requester → api_manager
    Conftest->>Conftest: Генерирует test_user
    TestFile->>AuthAPI: Вызов api_manager.auth_api.register_user(test_user)
    AuthAPI->>CustomRequester: Делегирует вызов send_request()
    CustomRequester->>RealAPI: Отправляет POST /register
    RealAPI-->>CustomRequester: Ответ {id, email, roles}
    CustomRequester-->>AuthAPI: Объект Response
    AuthAPI-->>TestFile: Возвращает response
    TestFile->>TestFile: Проверки (assert)
    TestFile-->>Pytest: Результат (Pass/Fail)'''
