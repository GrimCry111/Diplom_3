from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы входа"""
    
    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @name='password']")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(., 'Зарегистрироваться')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(., 'Восстановить пароль')]")