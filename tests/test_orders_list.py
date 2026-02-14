import allure
from helpers import OrderMethods
from data import OrderListData, OrderListMessages, OrderExpectedResponses


@allure.suite('Тесты на получение списка заказов')
class TestOrdersList:
    
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что запрос возвращает список заказов')
    def test_get_orders_list_success(self):
        with allure.step("Отправка запроса на получение списка заказов"):
            response = OrderMethods.get_orders_list()
        
        with allure.step("Проверка кода ответа"):
            assert response.status_code == OrderExpectedResponses.OK.status_code, \
                   f"Ожидался код {OrderExpectedResponses.OK.status_code}, получен {response.status_code}"
        
        with allure.step("Парсинг тела ответа"):
            response_body = response.json()
        
        with allure.step("Проверка наличия поля orders в ответе"):
            assert OrderListData.ORDERS_FIELD in response_body, \
                   OrderListMessages.MISSING_FIELD.format(OrderListData.ORDERS_FIELD)
        
        with allure.step("Проверка типа поля orders"):
            orders_list = response_body[OrderListData.ORDERS_FIELD]
            assert isinstance(orders_list, list), OrderListMessages.INVALID_ORDERS_TYPE
        
        with allure.step("Проверка структуры заказов"):
            if len(orders_list) > 0:
                with allure.step("Проверка первого заказа в списке"):
                    first_order = orders_list[0]
                    for field in OrderListData.REQUIRED_ORDER_FIELDS:
                        assert field in first_order, \
                               OrderListMessages.MISSING_FIELD_IN_ORDER.format(field)