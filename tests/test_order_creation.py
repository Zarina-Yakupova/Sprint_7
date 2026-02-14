import allure
import pytest
from helpers import OrderMethods
from data import OrderData, OrderMessages, OrderExpectedResponses


@allure.suite('Тесты на создание заказа')
class TestOrderCreation:
    
    @allure.title('Создание заказа с различными вариантами цвета')
    @allure.description('Параметризованный тест для проверки создания заказа с разными цветами самоката')
    @pytest.mark.parametrize('order_data', [
        OrderData.ORDER_WITH_BLACK_COLOR,
        OrderData.ORDER_WITH_GREY_COLOR,
        OrderData.ORDER_WITH_BOTH_COLORS,
        OrderData.ORDER_WITHOUT_COLOR
    ])
    def test_create_order_with_different_colors(self, order_data):
        with allure.step(f"Подготовка данных заказа с цветом: {order_data.get('color', [])}"):
            pass
        
        with allure.step("Отправка запроса на создание заказа"):
            response = OrderMethods.create_order(order_data)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == OrderExpectedResponses.CREATED.status_code, \
                   f"Ожидался код {OrderExpectedResponses.CREATED.status_code}, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля track в ответе"):
            response_body = response.json()
            assert "track" in response_body, OrderMessages.MISSING_FIELD.format("track")
        
        with allure.step("Проверка типа поля track"):
            assert isinstance(response_body["track"], int), OrderMessages.INVALID_TRACK_TYPE
    
    
    @allure.title('Создание стандартного заказа')
    @allure.description('Проверка создания заказа со стандартными параметрами')
    def test_create_default_order(self):
        with allure.step("Подготовка стандартных данных заказа"):
            pass
        
        with allure.step("Отправка запроса на создание заказа"):
            response = OrderMethods.create_order(OrderData.DEFAULT_ORDER)
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == OrderExpectedResponses.CREATED.status_code, \
                   f"Ожидался код {OrderExpectedResponses.CREATED.status_code}, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля track в ответе"):
            response_body = response.json()
            assert "track" in response_body, OrderMessages.MISSING_FIELD.format("track")
        
        with allure.step("Проверка типа поля track"):
            assert isinstance(response_body["track"], int), OrderMessages.INVALID_TRACK_TYPE