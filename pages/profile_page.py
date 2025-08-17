import allure
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    """Page Object для страницы профиля"""
    
    @allure.step("Переход по ссылке 'Профиль'")
    def click_profile_link(self):
        """Кликает по ссылке 'Профиль'"""
        self.wait_for_element_visibility(ProfilePageLocators.PROFILE_LINK)
        self.click_element(ProfilePageLocators.PROFILE_LINK)
    
    @allure.step("Переход по ссылке 'История заказов'")
    def click_order_history_link(self):
        """Кликает по ссылке 'История заказов'"""
        # Ожидаем появления ссылки
        self.wait_for_element_visibility(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
    
    @allure.step("Нажатие кнопки 'Выход'")
    def click_logout_button(self):
        """Кликает по кнопке 'Выход'"""
        # Ожидаем появления кнопки выхода
        self.wait_for_element_visibility(ProfilePageLocators.LOGOUT_BUTTON)
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
    
    @allure.step("Получение имени пользователя")
    def get_user_name(self):
        """Получает имя пользователя"""
        self.wait_for_element_visibility(ProfilePageLocators.USER_NAME)
        return self.get_attribute(ProfilePageLocators.USER_NAME, "value")
    
    @allure.step("Получение email пользователя")
    def get_user_email(self):
        """Получает email пользователя"""
        self.wait_for_element_visibility(ProfilePageLocators.USER_EMAIL)
        return self.get_attribute(ProfilePageLocators.USER_EMAIL, "value")
    
    @allure.step("Проверка видимости полей профиля")
    def is_profile_fields_visible(self):
        """Проверяет, что все поля профиля видны"""
        try:
            self.wait_for_element_visibility(ProfilePageLocators.NAME_FIELD)
            self.wait_for_element_visibility(ProfilePageLocators.EMAIL_FIELD)
            self.wait_for_element_visibility(ProfilePageLocators.PASSWORD_FIELD)
            return True
        except:
            return False
    
    @allure.step("Проверка видимости кнопок")
    def are_buttons_visible(self):
        """Проверяет, что кнопки 'Сохранить' и 'Отмена' видны"""
        try:
            self.wait_for_element_visibility(ProfilePageLocators.SAVE_BUTTON)
            self.wait_for_element_visibility(ProfilePageLocators.CANCEL_BUTTON)
            return True
        except:
            return False