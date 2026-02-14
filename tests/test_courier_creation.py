import allure
import requests
from urls import Urls
from data import CourierData
from helpers import CourierMethods


@allure.suite('Тесты на создание курьера')
class TestCourierCreation:
    
    @allure.title('Успешное создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается правильный ответ')
    def test_create_courier_success(self):
        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        response_body = response.json()
        assert "ok" in response_body, "В ответе отсутствует поле ok"
        assert response_body["ok"] == True, "Поле ok должно быть true"
    

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Проверка, что нельзя создать курьера с уже существующим логином')
    def test_create_duplicate_courier_failed(self, create_and_delete_courier):
        if create_and_delete_courier:
            payload = {
                "login": create_and_delete_courier["login"],
                "password": create_and_delete_courier["password"],
                "firstName": create_and_delete_courier["firstName"]
            }
            
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
            
            assert response.status_code == 409, f"Ожидался код 409, получен {response.status_code}"
            assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
    

    @allure.title('Создание курьера без обязательного поля "login"')
    @allure.description('Проверка, что нельзя создать курьера без логина')
    def test_create_courier_without_login_failed(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                data=CourierData.COURIER_WITHOUT_LOGIN)
        
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
    

    @allure.title('Создание курьера без обязательного поля "password"')
    @allure.description('Проверка, что нельзя создать курьера без пароля')
    def test_create_courier_without_password_failed(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                data=CourierData.COURIER_WITHOUT_PASSWORD)
        
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


    @allure.title('Создание курьера без обязательного поля "firstName"')
    @allure.description('Проверка, что можно создать курьера без имени')
    def test_create_courier_without_first_name_success(self):
        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        response_body = response.json()
        assert "ok" in response_body, "В ответе отсутствует поле ok"
        assert response_body["ok"] == True, "Поле ok должно быть true"
    

    @allure.title('Создание курьера с пустым телом запроса')
    @allure.description('Проверка, что нельзя создать курьера с пустым запросом')
    def test_create_courier_with_empty_body_failed(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                data=CourierData.EMPTY_BODY)
        
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
    

    @allure.title('Успешный запрос возвращает ok:true')
    @allure.description('Проверка, что при успешном создании курьера возвращается правильное тело ответа')
    def test_create_courier_return_ok_true(self):
        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        assert response.status_code == 201
        assert response.json()["ok"] == True
