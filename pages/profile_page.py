from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    """Page Object для страницы профиля"""
    
    def click_profile_link(self):
        """Кликает по ссылке 'Профиль'"""
        return self.click_element(ProfilePageLocators.PROFILE_LINK)
    
    def click_order_history_link(self):
        """Кликает по ссылке 'История заказов'"""
        return self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
    
    def click_logout_button(self):
        """Кликает по кнопке 'Выход'"""
        return self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
    
    def get_user_name(self):
        """Получает имя пользователя"""
        return self.get_text(ProfilePageLocators.USER_NAME)
    
    def get_user_email(self):
        """Получает email пользователя"""
        return self.get_text(ProfilePageLocators.USER_EMAIL)