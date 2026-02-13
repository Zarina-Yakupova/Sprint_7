import allure
from helpers import OrderMethods


@allure.suite('Тесты на получение списка заказов')
class TestOrdersList:
    
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что запрос возвращает список заказов')
    def test_get_orders_list_success(self):
        response = OrderMethods.get_orders_list()
        
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        
        response_body = response.json()
        assert "orders" in response_body, "В ответе отсутствует поле orders"
        assert isinstance(response_body["orders"], list), "Поле orders должно быть списком"
        assert len(response_body["orders"]) > 0, "Список заказов пуст"
        
        # Проверка структуры первого заказа
        if len(response_body["orders"]) > 0:
            first_order = response_body["orders"][0]
            required_fields = ["id", "courierId", "firstName", "lastName", "address", 
                             "metroStation", "phone", "rentTime", "deliveryDate", 
                             "track", "color", "comment", "createdAt", "updatedAt", "status"]
            
            for field in required_fields:
                assert field in first_order, f"В заказе отсутствует поле {field}"