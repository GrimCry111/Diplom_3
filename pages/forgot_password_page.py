from .base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    """Page Object для страницы восстановления пароля"""
    
    def enter_email(self, email):
        """Вводит email для восстановления пароля"""
        return self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)
    
    def click_restore_button(self):
        """Кликает по кнопке 'Восстановить'"""
        return self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
    
    def click_login_link(self):
        """Кликает по ссылке 'Войти'"""
        return self.click_element(ForgotPasswordPageLocators.LOGIN_LINK)
    
    def click_eye_button(self):
        """Кликает по кнопке 'Показать/скрыть пароль'"""
        return self.click_element(ForgotPasswordPageLocators.EYE_BUTTON)
    
    def is_password_field_active(self):
        """Проверяет, активно ли поле пароля после нажатия на 'глаз'"""
        try:
            # Проверяем, что поле пароля видимо
            self.wait_for_element_visibility(ForgotPasswordPageLocators.PASSWORD_INPUT)
            return True
        except:
            return False