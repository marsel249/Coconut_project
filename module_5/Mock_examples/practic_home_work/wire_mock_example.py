import requests
from module_5.Mock_examples.practic import WorldClockResponse, DateTimeRequest, WhatIsTodayResponse

#Modul_4\Cinescope\tests\api\test_mock_services.py
    #перед запсуком необходимо выполнить команду
    #docker run -it --rm -p 8080:8080 --name wiremock wiremock/wiremock:3.12.0
def run_wiremock_worldclockap_time():
# Запуск WireMock сервера (если используется standalone, этот шаг можно пропустить)
    wiremock_url = "http://localhost:8080/__admin/mappings"
    mapping = {
        "request": {
            "method": "GET",
            "url": "/wire/mock/api/json/utc/now"  # Эмулируем запрос к worldclockapi
        },
        "response": {
            "status": 200,
            "body": '''{
                "$id": "1",
                "currentDateTime": "2025-03-08T00:00Z",
                "utcOffset": "00:00",
                "isDayLightSavingsTime": false,
                "dayOfTheWeek": "Wednesday",
                "timeZoneName": "UTC",
                "currentFileTime": 1324567890123,
                "ordinalDate": "2025-1",
                "serviceResponse": null
            }'''
        }
    }
    response = requests.post(wiremock_url, json=mapping)
    assert response.status_code == 201, "Не удалось настроить WireMock"

def test_what_is_today_BY_WIREMOCK(): #Данный тест максимально похож на базовый
    # запускаем наш мок сервер
    run_wiremock_worldclockap_time()

    # Выполняем запрос к WireMock (имитация worldclockapi)
    world_clock_response = requests.get("http://localhost:8080/wire/mock/api/json/utc/now")
    assert world_clock_response.status_code == 200, "Удаленный сервис недоступен"
    # Парсим JSON-ответ с использованием Pydantic модели
    current_date_time = WorldClockResponse(**world_clock_response.json()).currentDateTime

    # Выполняем запрос к тестируемому сервису what_is_today
    what_is_today_response = requests.post(
        "http://127.0.0.1:16002/what_is_today",
        data=DateTimeRequest(currentDateTime=current_date_time).model_dump_json()
    )

    # Проверяем статус ответа от тестируемого сервиса
    assert what_is_today_response.status_code == 200, "Удаленный сервис недоступен"
    # Парсим JSON-ответ от тестируемого сервиса с использованием Pydantic модели
    what_is_today_data = WhatIsTodayResponse(**what_is_today_response.json())
    # Проверяем, что ответ соответствует ожидаемому
    assert what_is_today_data.message == "Международный женский день", "8 марта же?"