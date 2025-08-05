from selenium.webdriver.common.by import By

class ProfilePageLocators:
    """Локаторы для страницы профиля"""
    
    # Ссылки в профиле
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Информация о пользователе
    USER_NAME = (By.XPATH, "//input[@name='Name']")
    USER_EMAIL = (By.XPATH, "//input[@name='Почта']")