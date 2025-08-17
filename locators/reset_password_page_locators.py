from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    """Локаторы для страницы сброса пароля"""
    
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    
    # Кнопка "глаз"
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")