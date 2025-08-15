import allure
import requests
import random
import string
from urls import REGISTER_API_URL, USER_API_URL, INGREDIENTS_API_URL, ORDERS_API_URL

@allure.step("Генерация уникального email для тестов")
def generate_unique_email():
    """Генерирует уникальный email для тестов"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_string}@example.com"

@allure.step("Генерация случайного имени")
def generate_random_name():
    """Генерирует случайное имя"""
    return ''.join(random.choices(string.ascii_letters, k=8))

@allure.step("Создание нового пользователя через API")
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

@allure.step("Удаление пользователя через API")
def delete_user(token):
    """Удаляет пользователя через API"""
    if token:
        requests.delete(
            USER_API_URL,
            headers={"Authorization": token}
        )

@allure.step("Получение списка ингредиентов через API")
def get_ingredients():
    """Получает список ингредиентов из API"""
    response = requests.get(INGREDIENTS_API_URL)
    return response.json()["data"] if response.status_code == 200 else []

@allure.step("Оформление заказа через API")
def place_order(token, ingredients):
    """Оформляет заказ через API"""
    headers = {"Authorization": token}
    response = requests.post(ORDERS_API_URL, json={"ingredients": ingredients}, headers=headers)
    return response