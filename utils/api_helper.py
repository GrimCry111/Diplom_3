import requests
import random
import string
from urls import REGISTER_API_URL, USER_API_URL, INGREDIENTS_API_URL, ORDERS_API_URL

def generate_unique_email():
    """Генерирует уникальный email для тестов"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_string}@example.com"

def generate_random_name():
    """Генерирует случайное имя"""
    return ''.join(random.choices(string.ascii_letters, k=8))

def create_user():
    """Создает нового пользователя через API и возвращает данные и токен"""
    email = generate_unique_email()
    password = "password123"
    name = generate_random_name()
    
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    
    response = requests.post(REGISTER_API_URL, json=payload)
    if response.status_code == 200:
        return {
            "email": email,
            "password": password,
            "name": name,
            "token": response.json()["accessToken"]
        }
    return None

def delete_user(token):
    """Удаляет пользователя через API"""
    if token:
        requests.delete(
            USER_API_URL,
            headers={"Authorization": token}
        )

def get_ingredients():
    """Получает список ингредиентов из API"""
    response = requests.get(INGREDIENTS_API_URL)
    return response.json()["data"] if response.status_code == 200 else []

def place_order(token, ingredients):
    """Оформляет заказ через API"""
    headers = {"Authorization": token}
    response = requests.post(ORDERS_API_URL, json={"ingredients": ingredients}, headers=headers)
    return response