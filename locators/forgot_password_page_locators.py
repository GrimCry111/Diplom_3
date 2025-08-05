from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    
    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопки
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")