import requests
import random
import string

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def generate_unique_email():
    """Генерирует уникальный email для тестов"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_string}@example.com"

def create_user():
    """Создает нового пользователя через API и возвращает данные и токен"""
    email = generate_unique_email()
    password = "password123"
    name = "Test User"
    
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    
    response = requests.post(f"{BASE_URL}/auth/register", json=payload)
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
            f"{BASE_URL}/auth/user",
            headers={"Authorization": token}
        )