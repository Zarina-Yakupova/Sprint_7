import allure
import requests
import pytest
from urls import Urls
from data import CourierData, ErrorMessages, LoginPayloads


@allure.suite('Тесты на авторизацию курьера')
class TestCourierLogin:
    
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться и получает id')
    def test_login_courier_success(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера в фикстуре"):
            if not create_and_delete_courier:
                pytest.fail("Фикстура не создала курьера")
        
        with allure.step("Подготовка данных для авторизации"):
            payload = LoginPayloads.get_valid_payload(
                create_and_delete_courier["login"],
                create_and_delete_courier["password"]
            )
        
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        
        with allure.step("Проверка наличия id в ответе"):
            response_body = response.json()
            assert "id" in response_body, "В ответе отсутствует поле id"
        
        with allure.step("Проверка типа поля id"):
            assert isinstance(response_body["id"], int), "Поле id должно быть числом"
    

    @allure.title('Авторизация без поля "login"')
    @allure.description('Проверка, что нельзя авторизоваться без логина')
    def test_login_courier_without_login_failed(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера в фикстуре"):
            if not create_and_delete_courier:
                pytest.fail("Фикстура не создала курьера")
        
        with allure.step("Подготовка payload без поля login"):
            payload = LoginPayloads.without_login(create_and_delete_courier["password"])
        
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
        
        with allure.step("Проверка кода ответа (должен быть 400)"):
            assert response.status_code == 400, f"По документации ожидается код 400, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация без поля "password"')
    @allure.description('Проверка, что нельзя авторизоваться без пароля')
    def test_login_courier_without_password_failed(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера в фикстуре"):
            if not create_and_delete_courier:
                pytest.fail("Фикстура не создала курьера")
        
        with allure.step("Подготовка payload без поля password"):
            payload = LoginPayloads.without_password(create_and_delete_courier["login"])
        
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
        
        with allure.step("Проверка кода ответа (должен быть 400)"):
            assert response.status_code == 400, f"По документации ожидается код 400, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация с пустым телом запроса')
    @allure.description('Проверка, что нельзя авторизоваться с пустым запросом')
    def test_login_courier_with_empty_body_failed(self):
        with allure.step("Отправка запроса с пустым телом"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL,
                                    data=CourierData.EMPTY_BODY)
        
        with allure.step("Проверка кода ответа (должен быть 400)"):
            assert response.status_code == 400, f"По документации ожидается код 400, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA_FOR_LOGIN
    

    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что нельзя авторизоваться с неправильным логином')
    def test_login_courier_invalid_login_failed(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера в фикстуре"):
            if not create_and_delete_courier:
                pytest.fail("Фикстура не создала курьера")
        
        with allure.step("Подготовка payload с неверным логином"):
            payload = LoginPayloads.invalid_login(
                create_and_delete_courier["password"]
            )
        
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
        
        with allure.step("Проверка кода ответа (должен быть 404)"):
            assert response.status_code == 404, f"По документации ожидается код 404, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND
    

    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что нельзя авторизоваться с неправильным паролем')
    def test_login_courier_invalid_password_failed(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера в фикстуре"):
            if not create_and_delete_courier:
                pytest.fail("Фикстура не создала курьера")
        
        with allure.step("Подготовка payload с неверным паролем"):
            payload = LoginPayloads.invalid_password(
                create_and_delete_courier["login"]
            )
        
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, data=payload)
        
        with allure.step("Проверка кода ответа (должен быть 404)"):
            assert response.status_code == 404, f"По документации ожидается код 404, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND
    
    
    @allure.title('Авторизация несуществующего пользователя')
    @allure.description('Проверка, что нельзя авторизоваться под несуществующим пользователем')
    def test_login_nonexistent_courier_failed(self):
        with allure.step("Отправка запроса на авторизацию с неверными данными"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_URL, 
                                    data=CourierData.INVALID_CREDENTIALS)
        
        with allure.step("Проверка кода ответа (должен быть 404)"):
            assert response.status_code == 404, f"По документации ожидается код 404, получен {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND