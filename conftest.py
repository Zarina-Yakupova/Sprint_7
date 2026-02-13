import pytest
import requests
from urls import Urls
from helpers import CourierMethods


@pytest.fixture
def create_and_delete_courier():
    """Фикстура для создания и удаления курьера"""
    courier_data = CourierMethods.register_new_courier_and_return_login_password()
    
    if courier_data:
        login, password, first_name = courier_data
        
        yield {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        # Авторизация для получения ID курьера
        auth_payload = {
            "login": login,
            "password": password
        }
        auth_response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=auth_payload)
        
        if auth_response.status_code == 200:
            courier_id = auth_response.json()["id"]
            CourierMethods.delete_courier(courier_id)
    else:
        yield None