class CourierData:
    COURIER_WITHOUT_LOGIN = {
        "password": "1234",
        "firstName": "miuki"
    }
    
    COURIER_WITHOUT_PASSWORD = {
        "login": "meika",
        "firstName": "miuki"
    }
    
    COURIER_WITHOUT_FIRST_NAME = {
        "login": "meika",
        "password": "1234"
    }
    
    EMPTY_BODY = {}
    
    INVALID_CREDENTIALS = {
        "login": "invalid_login",
        "password": "invalid_password"
    }


class OrderData:
    DEFAULT_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
    
    ORDER_WITH_BLACK_COLOR = {
        **DEFAULT_ORDER,
        "color": ["BLACK"]
    }
    
    ORDER_WITH_GREY_COLOR = {
        **DEFAULT_ORDER,
        "color": ["GREY"]
    }
    
    ORDER_WITH_BOTH_COLORS = {
        **DEFAULT_ORDER,
        "color": ["BLACK", "GREY"]
    }
    
    ORDER_WITHOUT_COLOR = {
        **DEFAULT_ORDER,
        "color": []
    }


class ErrorMessages:

    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
    COURIER_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    INSUFFICIENT_DATA_FOR_LOGIN = "Недостаточно данных для входа"


class LoginPayloads:
    
    @staticmethod
    def get_valid_payload(login, password):
        return {
            "login": login,
            "password": password
        }
    
    @staticmethod
    def without_login(password):
        return {
            "password": password
        }
    
    @staticmethod
    def without_password(login):
        return {
            "login": login
        }
    
    @staticmethod
    def invalid_login(password):
        return {
            "login": "invalid_login_" + ''.join(__import__('random').choices(__import__('string').ascii_lowercase, k=5)),
            "password": password
        }
    
    @staticmethod
    def invalid_password(login):
        return {
            "login": login,
            "password": "invalid_password_" + ''.join(__import__('random').choices(__import__('string').ascii_lowercase, k=5))
        }
    
class OrderMessages:
    MISSING_FIELD = "В ответе отсутствует поле {}"
    MISSING_ERROR_MESSAGE = "В ответе отсутствует сообщение об ошибке"
    INVALID_TRACK_TYPE = "Поле track должно быть числом"


class OrderExpectedResponses:
    
    class CREATED:
        status_code = 201
        required_fields = ["track"]

    class OK:  
        status_code = 200
        required_fields = ["orders"]
    

class OrderListData:
    
    ORDERS_FIELD = "orders"
    
    REQUIRED_ORDER_FIELDS = [
        "id", "courierId", "firstName", "lastName", "address", 
        "metroStation", "phone", "rentTime", "deliveryDate", 
        "track", "color", "comment", "createdAt", "updatedAt", "status"
    ]
    
    TEST_LIMIT = 5
    INVALID_LIMIT = -1
    TEST_PAGE = 2


class OrderListMessages:
    
    MISSING_FIELD = "В ответе отсутствует поле {}"
    MISSING_FIELD_IN_ORDER = "В заказе отсутствует поле {}"
    INVALID_ORDERS_TYPE = "Поле orders должно быть списком"
    LIMIT_EXCEEDED = "Количество заказов превышает указанный лимит"
    EMPTY_ORDERS_LIST = "Список заказов пуст"