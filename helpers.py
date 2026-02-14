import requests
import random
import string
from urls import Urls


class CourierMethods:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    @staticmethod
    def register_new_courier_and_return_login_password():
        login_pass = []
        
        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE_URL, data=payload, timeout=30)
        
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        
        return login_pass
    
    @staticmethod
    def delete_courier(courier_id):
        response = requests.delete(f"{Urls.BASE_URL}{Urls.COURIER_CREATE_URL}/{courier_id}")
        return response


class OrderMethods:
    @staticmethod
    def create_order(order_data):
        response = requests.post(Urls.BASE_URL + Urls.ORDER_CREATE_URL, json=order_data)
        return response
    
    @staticmethod
    def get_orders_list():
        response = requests.get(Urls.BASE_URL + Urls.ORDER_LIST_URL)
        return response