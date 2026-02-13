import allure
import pytest
from helpers import OrderMethods
from data import OrderData


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
        response = OrderMethods.create_order(order_data)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле track"
        assert isinstance(response.json()["track"], int), "Поле track должно быть числом"
    
    @allure.title('Создание стандартного заказа')
    @allure.description('Проверка создания заказа со стандартными параметрами')
    def test_create_default_order(self):
        response = OrderMethods.create_order(OrderData.DEFAULT_ORDER)
        
        assert response.status_code == 201
        assert "track" in response.json()