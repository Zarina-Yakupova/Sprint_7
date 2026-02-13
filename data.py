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
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    
    ORDER_WITH_GREY_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
    }
    
    ORDER_WITH_BOTH_COLORS = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GREY"]
    }
    
    ORDER_WITHOUT_COLOR = {
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