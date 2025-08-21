
# #Работающий вариант псевдокода
# # test_weather_minimal.py
# from unittest.mock import Mock
#
# # «Реальный» сервис (в тесте не вызываем)
# class ThermometerServise:
#     def get_weather(self, city) -> int:
#         # здесь был бы вызов внешнего API:
#         # return gismeteo_client.request_weather(city)
#         raise NotImplementedError # можно заменить на pass
#
# # Небольшой сервис с бизнес-логикой
# class MyService:
#     def check_temperature(self, temperature: int) -> bool:
#         return temperature >= 30
#
# my_service = MyService()
#
# # Мок внешнего сервиса
# gismeteo_mock = Mock(spec=ThermometerServise)
# gismeteo_mock.get_weather.return_value = 100  # любой город -> 100
#
# def test_fetch_data():
#     # Используем мок вместо реального клиента
#     temperature = gismeteo_mock.get_weather("Moscow")
#     assert temperature == 100  # мок работает
#
#     result = my_service.check_temperature(temperature)
#     assert result is True
#
#     # Плюс проверим, что метод вызывался как надо
#     gismeteo_mock.get_weather.assert_called_once_with("Moscow")



# #Работающий вариант псевдокода, мок последовательно возвращает температуру: -100, 0, 100, и реализацией цикла ответа мока
# from unittest.mock import Mock, call
# from itertools import cycle #для того, чтобы зациклить мок
#
# # «Реальный» сервис (в тесте не вызываем)
# class ThermometerServise:
#     def get_weather(self, city) -> int:
#         # здесь был бы вызов внешнего API:
#         # return gismeteo_client.request_weather(city)
#         raise NotImplementedError
#
# # Небольшой сервис с бизнес-логикой
# class MyService:
#     def check_temperature(self, temperature: int) -> bool:
#         return temperature >= 30
#
# my_service = MyService()
#
# # Мок внешнего сервиса
# gismeteo_mock = Mock(spec=ThermometerServise)
# # gismeteo_mock.get_weather.return_value = 100  # любой город -> 100
# # gismeteo_mock.get_weather.side_effect = [-100, 0, 100] # Последовательно возвращает -100, 0, 100
# gismeteo_mock.get_weather.side_effect = cycle([-100, 0, 100]) # Бесконечным циклом возвращает -100, 0, 100, -100, 0...
#
#
# def test_fetch_data():
#     # Используем мок вместо реального клиента
#     t1 = gismeteo_mock.get_weather("Moscow")
#     t2 = gismeteo_mock.get_weather("Moscow")
#     t3 = gismeteo_mock.get_weather("Moscow")
#     t4 = gismeteo_mock.get_weather("Moscow")
#
#
#     assert (t1, t2, t3, t4) == (-100, 0, 100, -100) # Для проверки бесконечного цикла добавлен t4
#
#     # Проверим бизнес-логику
#     assert my_service.check_temperature(t1) is False
#     assert my_service.check_temperature(t2) is False
#     assert my_service.check_temperature(t3) is True
#     assert my_service.check_temperature(t4) is False
#
#     # И что вызывались три раза именно с "Moscow"
#     assert gismeteo_mock.get_weather.call_args_list == [
#         call("Moscow"),
#         call("Moscow"),
#         call("Moscow"),
#         call("Moscow"),
#     ]



# #Работающий вариант псевдокода, мок последовательно возвращает температуру: -100, 0, 100, реализацией цикла,
# # От выбранного города зависит температура, которую отдает мок
# from unittest.mock import Mock, call
# from itertools import cycle #для того, чтобы зациклить мок
#
# # «Реальный» сервис (в тесте не вызываем)
# class ThermometerServise:
#     def get_weather(self, city) -> int:
#         # здесь был бы вызов внешнего API:
#         # return gismeteo_client.request_weather(city)
#         raise NotImplementedError
#
# # Небольшой сервис с бизнес-логикой
# class MyService:
#     def check_temperature(self, temperature: int) -> bool:
#         return temperature >= 30
#
# my_service = MyService()
#
# # Мок внешнего сервиса
# def by_city(city):
#     return {'Moscow': 20, 'Rome': 35, 'Paris': 50}[city]
#
# gismeteo_mock = Mock(spec=ThermometerServise)
# # gismeteo_mock.get_weather.return_value = 100  # любой город -> 100
# # gismeteo_mock.get_weather.side_effect = [-100, 0, 100] # Последовательно возвращает -100, 0, 100
# #gismeteo_mock.get_weather.side_effect = cycle([-100, 0, 100]) # Бесконечным циклом возвращает -100, 0, 100, -100, 0...
# gismeteo_mock.get_weather.side_effect = by_city # Поведение мока зависит от выбранного города
#
# def test_fetch_data():
#     # Используем мок вместо реального клиента
#     t1 = gismeteo_mock.get_weather("Moscow")
#     t2 = gismeteo_mock.get_weather("Rome")
#     t3 = gismeteo_mock.get_weather("Paris")
#     t4 = gismeteo_mock.get_weather("Moscow")
#
#
#     assert (t1, t2, t3, t4) == (20, 35, 50, 20)
#
#     # Проверим бизнес-логику
#     assert my_service.check_temperature(t1) is False
#     assert my_service.check_temperature(t2) is True
#     assert my_service.check_temperature(t3) is True
#     assert my_service.check_temperature(t4) is False
#
#     # И что вызывались три раза именно с "Moscow"
#     assert gismeteo_mock.get_weather.call_args_list == [
#         call("Moscow"),
#         call("Rome"),
#         call("Paris"),
#         call("Moscow"),
#     ]


'''Stab (Заглушка)'''
# class Database:
#     def get_user(self, user_id):
#         # Реальный код для получения пользователя из базы данных
#         pass
#
# import pytest
# '''возвращает одного и того же пользователя, независимо от переданного user_id. '''
# class StubDatabase:
#     def get_user(self, user_id):
#         return {"id": user_id, "name": "John Doe"}
#
# def test_get_user():
#     db = StubDatabase()
#     user = db.get_user(1)
#     assert user["name"] == "John Doe"


'''Mock - 
 позволяет проверять, как и с какими аргументами вызывались его методы.'''
# class EmailService:
#     def send_email(self, to, subject, body):
#         # Реальный код для отправки email
#         pass
#
# from unittest.mock import Mock, create_autospec
#
# def test_send_email():
#     # email_service = Mock() # Вариант из notion
#     email_service = Mock(spec_set=EmailService)
#     # email_service = create_autospec(EmailService, spec_set=True, instance=True) #Самая надежная версия
#     email_service.send_email("user@example.com", "Hello", "This is a test email")
#
#     email_service.send_email.assert_called_once_with("user@example.com", "Hello", "This is a test email")



from unittest.mock import Mock, create_autospec

class EmailService:
    def send_email(self, to, subject, body):
        # Реальный код для отправки email
        pass

class Notifier:
    def __init__(self, email_service):
        self.email_service = email_service

    def welcome(self, user_email):
        self.email_service.send_email(user_email, "Hello", "Welcome!")

def test_notifier_welcome():
    email_service = create_autospec(EmailService, spec_set=True, instance=True) # Делаем мок
    notifier = Notifier(email_service)

    notifier.welcome("user@example.com")

    email_service.send_email.assert_called() # Проверяет, что мок был вызван
    email_service.send_email.assert_called_once() # Проверяет, что мок был вызван - один раз


    email_service.send_email.assert_called_once_with(
        "user@example.com", "Hello", "Welcome!"
    ) # Проверяет, что мок был вызван один раз, с определенными параметрами

    email_service.reset_mock() # Очищаем историю вызовов мока
    email_service.send_email.assert_not_called() # Проверка на то, что мок не вызывался






