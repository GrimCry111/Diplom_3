from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, "//button[contains(., 'Восстановить')]")
    
    # Поле ввода пароля (на странице сброса пароля)
    # ИСПРАВЛЕНИЕ: Используем поиск по тексту label вместо атрибута name
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Кнопка "глаз"
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")