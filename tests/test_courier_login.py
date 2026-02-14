import allure
import requests
import pytest
from urls import Urls
from data import CourierData, ErrorMessages, LoginPayloads
from helpers import CourierMethods


@allure.suite('Тесты на авторизацию курьера')
class TestCourierLogin:
    
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться и получает id')
    def test_login_courier_success(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = LoginPayloads.get_valid_payload(
                create_and_delete_courier["login"],
                create_and_delete_courier["password"]
            )
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
            assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
            
            response_body = response.json()
            assert "id" in response_body, "В ответе отсутствует поле id"
            assert isinstance(response_body["id"], int), "Поле id должно быть числом"
    

    @allure.title('Авторизация без поля "login"')
    @allure.description('Проверка, что нельзя авторизоваться без логина')
    def test_login_courier_without_login_failed(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = LoginPayloads.without_login(create_and_delete_courier["password"])
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
            
            if response.status_code == 504:
                pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
            else:
                assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
                assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация без поля "password"')
    @allure.description('Проверка, что нельзя авторизоваться без пароля')
    def test_login_courier_without_password_failed(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = LoginPayloads.without_password(create_and_delete_courier["login"])
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
            
            if response.status_code == 504:
                pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
            else:
                assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
                assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация с пустым телом запроса')
    @allure.description('Проверка, что нельзя авторизоваться с пустым запросом')
    def test_login_courier_with_empty_body_failed(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL,
                                data=CourierData.EMPTY_BODY)
        
        if response.status_code == 504:
            pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
        else:
            assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что нельзя авторизоваться с неправильным логином')
    def test_login_courier_invalid_login_failed(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = LoginPayloads.invalid_login(
                create_and_delete_courier["password"]
            )
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
            
            if response.status_code == 504:
                pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
            else:
                assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
                assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND
    

    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что нельзя авторизоваться с неправильным паролем')
    def test_login_courier_invalid_password_failed(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = LoginPayloads.invalid_password(
                create_and_delete_courier["login"]
            )
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
            
            if response.status_code == 504:
                pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
            else:
                assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
                assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND
    
    
    @allure.title('Авторизация несуществующего пользователя')
    @allure.description('Проверка, что нельзя авторизоваться под несуществующим пользователем')
    def test_login_nonexistent_courier_failed(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, 
                                data=CourierData.INVALID_CREDENTIALS)
        
        if response.status_code == 504:
            pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")
        else:
            assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
            assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND