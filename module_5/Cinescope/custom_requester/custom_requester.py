#
# import json
# import logging
# import os
# from pydantic import BaseModel
# from module_5.Cinescope.constants import RED, GREEN, RESET
#
# class CustomRequester:
#     """
#     Кастомный реквестер для стандартизации и упрощения отправки HTTP-запросов.
#     """
#
#
#
#     base_headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }
#
#     def __init__(self, session, base_url):
#         self.session = session
#         self.base_url = base_url
#         self.headers = self.base_headers.copy()
#         self.logger = logging.getLogger(__name__)
#         self.logger.setLevel(logging.INFO)
#
#     #Версия до рефакторинга
#     # def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
#     #     url = f"{self.base_url}{endpoint}"
#     #     response = self.session.request(method, url, json=data)
#     #     if need_logging:
#     #         self.log_request_and_response(response)
#     #     if response.status_code != expected_status:
#     #         raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")
#     #     return response
#
#
#     def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True, params=None):
#         """
#         Универсальный метод для отправки запросов.
#         :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.).
#         :param endpoint: Эндпоинт (например, "/login").
#         :param data: Тело запроса (JSON-данные).
#         :param expected_status: Ожидаемый статус-код (по умолчанию 200).
#         :param need_logging: Флаг для логирования (по умолчанию True).
#         :return: Объект ответа requests.Response.
#         """
#         url = f"{self.base_url}{endpoint}"
#         response = self.session.request(method, url, json=data, headers=self.headers, params=params) #Добавили заголовки
#         if need_logging:
#             self.log_request_and_response(response)
#         if response.status_code != expected_status:
#             raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")
#
#         if isinstance(data, BaseModel):
#             data = json.loads(data.model_dump_json(exclude_unset=True))
#         response = self.session.request(method, url, json=data, params=params)
#
#         # if isinstance(expected_status, (list, tuple, set)):
#         #     if response.status_code not in expected_status:
#         #         raise ValueError(f"Unexpected status code: {response.status_code}. Expected one of: {expected_status}")
#         # else:
#         #     if response.status_code != expected_status:
#         #         raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")
#         return response
#
#
#     '''def log_request_and_response(self, response):
#         try:
#             request = response.request
#             GREEN = '\033[32m'
#             RED = '\033[31m'
#             RESET = '\033[0m'
#             headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
#             full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"
#
#             body = ""
#             if hasattr(request, 'body') and request.body is not None:
#                 if isinstance(request.body, bytes):
#                     body = request.body.decode('utf-8')
#                 body = f"-d '{body}' \n" if body != '{}' else ''
#
#             self.logger.info(f"\n{'=' * 40} REQUEST {'=' * 40}")
#             self.logger.info(
#                 f"{GREEN}{full_test_name}{RESET}\n"
#                 f"curl -X {request.method} '{request.url}' \\\n"
#                 f"{headers} \\\n"
#                 f"{body}"
#             )
#
#             response_data = response.text
#             try:
#                 response_data = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
#             except json.JSONDecodeError:
#                 pass
#
#             self.logger.info(f"\n{'=' * 40} RESPONSE {'=' * 40}")
#             if not response.ok:
#                 self.logger.info(
#                     f"\tSTATUS_CODE: {RED}{response.status_code}{RESET}\n"
#                     f"\tDATA: {RED}{response_data}{RESET}"
#                 )
#             else:
#                 self.logger.info(
#                     f"\tSTATUS_CODE: {GREEN}{response.status_code}{RESET}\n"
#                     f"\tDATA:\n{response_data}"
#                 )
#             self.logger.info(f"{'=' * 80}\n")
#         except Exception as e:
#             self.logger.error(f"\nLogging failed: {type(e)} - {e}")'''
#
#     def log_request_and_response(self, response):
#         """
#         Логгирование запросов и ответов. Настройки логгирования описаны в pytest.ini
#         Преобразует вывод в curl-like (-H хэдэеры), (-d тело)
#
#         :param response: Объект response получаемый из метода "send_request"
#         """
#         try:
#             request = response.request
#             headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
#             full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"
#
#             body = ""
#             if hasattr(request, 'body') and request.body is not None:
#                 if isinstance(request.body, bytes):
#                     body = request.body.decode('utf-8')
#                 elif isinstance(request.body, str):
#                     body = request.body
#                 body = f"-d '{body}' \n" if body != '{}' else ''
#
#             self.logger.info(
#                 f"{GREEN}{full_test_name}{RESET}\n"
#                 f"curl -X {request.method} '{request.url}' \\\n"
#                 f"{headers} \\\n"
#                 f"{body}"
#             )
#
#             response_status = response.status_code
#             is_success = response.ok
#             response_data = response.text
#             if not is_success:
#                 self.logger.info(f"\tRESPONSE:"
#                                  f"\nSTATUS_CODE: {RED}{response_status}{RESET}"
#                                  f"\nDATA: {RED}{response_data}{RESET}")
#         except Exception as e:
#             self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")
#
#
# #Добаввление после рефакторинга
#
#     def _update_session_headers(self, **kwargs): #убрал session
#     # def _update_session_headers(self, session, **kwargs): #убрал session
#         """
#         Обновление заголовков сессии.
#         :param session: Объект requests.Session, предоставленный API-классом.
#         :param kwargs: Дополнительные заголовки.
#         """
#         self.headers.update(kwargs)  # Обновляем базовые заголовки
#         self.session.headers.update(self.headers)  # Обновляем заголовки в текущей сессии
#         # session.headers.update(self.headers)  # Обновляем заголовки в текущей сессии

# module_5/Cinescope/custom_requester/custom_requester.py
import os
import json
import logging
from pydantic import BaseModel
from module_5.Cinescope.constants import RED, GREEN, RESET, CYAN
from typing import Any, Iterable



class CustomRequester:
    def __init__(self, session, base_url: str, default_headers: dict | None = None):
        self.session = session
        self.base_url = base_url.rstrip("/")
        self.logger = logging.getLogger(__name__)

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if default_headers:
            self.headers.update(default_headers)
        self.session.headers.update(self.headers)

    def send_request(self, method: str, endpoint: str, data=None,
                     expected_status: int |Iterable[int]| None = None, params=None, token=None):
        url = f"{self.base_url}{endpoint}"

        # Подготовка payload
        if isinstance(data, BaseModel):
            payload = data.model_dump(mode="json", exclude_none=True)
        elif isinstance(data, dict):
            payload = {k: v for k, v in data.items() if v is not None}
        else:
            payload = data

        #Добавляем токен в хедеры, если его передали в запросе
        req_headers = None
        if token is not None:
            req_headers = dict(self.session.headers)
            req_headers['Authorization'] = f'Bearer {token}'


        # Выполняем запрос
        resp = self.session.request(method=method.upper(), url=url, json=payload, params=params, headers=req_headers)

        # Лог запроса/ответа
        self.log_request_and_response(resp)

        # # Проверка ожидаемого статуса
        # if expected_status is not None and resp.status_code != expected_status:
        #     try:
        #         body = resp.json()
        #     except Exception:
        #         body = resp.text
        #     raise AssertionError(
        #         f"Unexpected status {resp.status_code} for {method} {endpoint}; "
        #         f"expected {expected_status}. Body: {body}"
        #     )
        # return resp

        #Эта логика позволяет использовать кортежи, словари, множества, в expected_status
        if expected_status is not None:
            if isinstance(expected_status, int):
                allowed = {expected_status}
            elif isinstance(expected_status, (tuple, list, set)):
                allowed = set(expected_status)
            else:
                raise TypeError(
                    f"expected_status must be int, tuple/list/set of ints, or None. Got: {type(expected_status)}"
                )

            if resp.status_code not in allowed:
                try:
                    body = resp.json()
                except Exception:
                    body = resp.text
                raise AssertionError(
                    f"Unexpected status {resp.status_code} for {method} {endpoint}; "
                    f"expected {sorted(allowed)}. Body: {body}"
                )

        return resp

    def _update_session_headers(self, **kwargs):
        self.headers.update(kwargs)
        self.session.headers.update(kwargs)

    def log_request_and_response(self, response):
        """
        Детальный лог: имя теста, curl-команда, статус/время, ключевые поля JSON.
        Токены (accessToken/refreshToken) выводятся ПОЛНОСТЬЮ.
        """
        try:
            req = response.request
            headers = " \\\n".join([f"-H '{h}: {v}'" for h, v in req.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""
            if hasattr(req, "body") and req.body is not None:
                if isinstance(req.body, bytes):
                    body_str = req.body.decode("utf-8")
                elif isinstance(req.body, str):
                    body_str = req.body
                else:
                    try:
                        body_str = json.dumps(req.body, ensure_ascii=False)
                    except Exception:
                        body_str = str(req.body)
                body = f"-d '{body_str}' \n" if body_str != "{}" else ""

            # curl-представление запроса
            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {req.method} '{req.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            status = response.status_code
            elapsed_ms = None
            if hasattr(response, "elapsed") and response.elapsed:
                try:
                    elapsed_ms = int(response.elapsed.total_seconds() * 1000)
                except Exception:
                    elapsed_ms = None

            # Пытаемся распарсить JSON
            json_body: dict[str, Any] | None = None
            try:
                json_body = response.json()
                if not isinstance(json_body, dict):
                    json_body = None
            except Exception:
                json_body = None

            summary_lines = [
                f"{CYAN}RESPONSE SUMMARY{RESET}",
                f"STATUS_CODE: {status}" + (f" | TIME: {elapsed_ms} ms" if elapsed_ms is not None else "")
            ]

            if json_body:
                # Если это логин — добавим email/roles/id
                if "/login" in req.url:
                    user = json_body.get("user", {})
                    email = user.get("email")
                    roles = user.get("roles")
                    user_id = user.get("id")
                    if email:
                        summary_lines.append(f"USER_EMAIL: {email}")
                    if roles:
                        summary_lines.append(f"USER_ROLES: {roles}")
                    if user_id:
                        summary_lines.append(f"USER_ID: {user_id}")

                # ВСЕГДА печатаем токены ПОЛНОСТЬЮ, если есть
                if "accessToken" in json_body:
                    summary_lines.append(f"ACCESS_TOKEN: {json_body['accessToken']}")
                if "refreshToken" in json_body:
                    summary_lines.append(f"REFRESH_TOKEN: {json_body['refreshToken']}")

                # Превью остального JSON
                summary_lines.append("JSON_PREVIEW: " + self._pretty_preview(json_body, limit=800))

            self.logger.info("\n".join(summary_lines))

            # При ошибках — сырой ответ полностью
            if not response.ok:
                self.logger.info(
                    f"\n\tRESPONSE RAW:"
                    f"\nSTATUS_CODE: {RED}{status}{RESET}"
                    f"\nDATA: {RED}{response.text}{RESET}"
                )

        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")

    def _pretty_preview(self, obj: Any, limit: int = 800) -> str:
        try:
            text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), indent=None)
        except Exception:
            text = str(obj)
        if len(text) > limit:
            return text[:limit] + f"... (+{len(text)-limit} chars)"
        return text



