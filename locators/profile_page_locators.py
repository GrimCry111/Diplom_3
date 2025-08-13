from selenium.webdriver.common.by import By

class ProfilePageLocators:
    """Локаторы для страницы профиля"""
    
    # Используем contains() вместо точного совпадения
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/account')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(., 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выход')]")
    
    # Добавляем локатор для имени пользователя
    USER_NAME = (By.XPATH, "//input[@name='Name']")
    
    # Добавляем локатор для email
    USER_EMAIL = (By.XPATH, "//input[@name='Email']")

    # Поля профиля
    NAME_FIELD = (By.XPATH, "//input[@name='Name']")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Логин']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # Кнопки
    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Сохранить')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(., 'Отмена')]")