import allure
import requests
from urls import Urls
from data import CourierData, ErrorMessages
from helpers import CourierMethods


@allure.suite('Тесты на создание курьера')
class TestCourierCreation:
    
    @allure.title('Успешное создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается правильный ответ')
    def test_create_courier_success(self):
        with allure.step("Генерация данных нового курьера"):
            login = CourierMethods.generate_random_string(10)
            password = CourierMethods.generate_random_string(10)
            first_name = CourierMethods.generate_random_string(10)
            
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }
        
        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        with allure.step("Проверка тела ответа"):
            response_body = response.json()
            assert "ok" in response_body, "В ответе отсутствует поле ok"
            assert response_body["ok"] == True, "Поле ok должно быть true"
    

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Проверка, что нельзя создать курьера с уже существующим логином')
    def test_create_duplicate_courier_failed(self, create_and_delete_courier):
        with allure.step("Проверка наличия созданного курьера"):
            if not create_and_delete_courier:
                allure.skip("Курьер не был создан")
                return
        
        with allure.step("Подготовка payload с существующим логином"):
            payload = {
                "login": create_and_delete_courier["login"],
                "password": create_and_delete_courier["password"],
                "firstName": create_and_delete_courier["firstName"]
            }
        
        with allure.step("Отправка запроса на создание дубликата курьера"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 409, f"Ожидался код 409, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.COURIER_ALREADY_EXISTS
    

    @allure.title('Создание курьера без обязательного поля "login"')
    @allure.description('Проверка, что нельзя создать курьера без логина')
    def test_create_courier_without_login_failed(self):
        with allure.step("Отправка запроса без поля login"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                    data=CourierData.COURIER_WITHOUT_LOGIN)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA
    

    @allure.title('Создание курьера без обязательного поля "password"')
    @allure.description('Проверка, что нельзя создать курьера без пароля')
    def test_create_courier_without_password_failed(self):
        with allure.step("Отправка запроса без поля password"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                    data=CourierData.COURIER_WITHOUT_PASSWORD)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA
    

    @allure.title('Создание курьера без обязательного поля "firstName"')
    @allure.description('Проверка, что можно создать курьера без имени')
    def test_create_courier_without_first_name_success(self):
        with allure.step("Генерация данных курьера без имени"):
            login = CourierMethods.generate_random_string(10)
            password = CourierMethods.generate_random_string(10)
            
            payload = {
                "login": login,
                "password": password
            }
        
        with allure.step("Отправка запроса на создание курьера без имени"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        with allure.step("Проверка тела ответа"):
            response_body = response.json()
            assert "ok" in response_body, "В ответе отсутствует поле ok"
            assert response_body["ok"] == True, "Поле ok должно быть true"
    

    @allure.title('Создание курьера с пустым телом запроса')
    @allure.description('Проверка, что нельзя создать курьера с пустым запросом')
    def test_create_courier_with_empty_body_failed(self):
        with allure.step("Отправка запроса с пустым телом"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, 
                                    data=CourierData.EMPTY_BODY)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ErrorMessages.INSUFFICIENT_DATA
    
    
    @allure.title('Успешный запрос возвращает ok:true')
    @allure.description('Проверка, что при успешном создании курьера возвращается правильное тело ответа')
    def test_create_courier_return_ok_true(self):
        with allure.step("Генерация данных нового курьера"):
            login = CourierMethods.generate_random_string(10)
            password = CourierMethods.generate_random_string(10)
            first_name = CourierMethods.generate_random_string(10)
            
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }
        
        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        with allure.step("Проверка поля ok в ответе"):
            assert response.json()["ok"] == True, "Поле ok должно быть true"