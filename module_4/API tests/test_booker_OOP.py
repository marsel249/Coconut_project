import pytest
from constants import BASE_URL

class TestBookings:
    def test_create_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_change_booking(self, auth_session, booking_data, new_booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data[
            "totalprice"], "Заданная стоимость не совпадает"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        change_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=new_booking_data)
        assert change_booking.status_code == 200, "Ошибка при изменении брони"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        # assert change_booking.json() != create_booking.json(), "JSON при бронировании, и его изменении - идентичны"
        assert get_booking.json()["lastname"] != booking_data["lastname"], "Заданная фамилия совпадает"
        assert get_booking.json()["firstname"] != booking_data["firstname"], "Заданное имя совпадает"
        assert get_booking.json()["totalprice"] != booking_data["totalprice"], "Заданная стоимость совпадает"
        assert get_booking.json()["depositpaid"] != booking_data["depositpaid"], "Заданная депозит совпадает"
        assert get_booking.json()["bookingdates"] != booking_data["bookingdates"], "Заданные даты совпадают"
        assert get_booking.json()["additionalneeds"] != booking_data["additionalneeds"], "Заданные допы совпадают"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"


    def test_something_change_booking(self, auth_session, booking_data, patch_booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data[
            "totalprice"], "Заданная стоимость не совпадает"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        change_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_booking_data)
        assert change_booking.status_code == 200, "Ошибка при изменении брони"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        # assert change_booking.json() != create_booking.json(), "JSON при бронировании, и его изменении - идентичны"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия НЕ совпадает(в patch не обновляли)"
        assert get_booking.json()["firstname"] != booking_data["firstname"], "Заданное имя совпадает"
        assert get_booking.json()["totalprice"] == booking_data["totalprice"], "Заданная стоимость НЕ совпадает(в patch не обновляли)"
        assert get_booking.json()["depositpaid"] == booking_data["depositpaid"], "Заданная депозит НЕ совпадает(в patch не обновляли)"
        assert get_booking.json()["bookingdates"] == booking_data["bookingdates"], "Заданные даты НЕ совпадают(в patch не обновляли)"
        assert get_booking.json()["additionalneeds"] != booking_data["additionalneeds"], "Заданные допы совпадают"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"


