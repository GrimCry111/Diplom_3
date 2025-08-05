from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    """Page Object для страницы входа"""
    
    def enter_email(self, email):
        """Вводит email в поле"""
        return self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """Вводит пароль в поле"""
        return self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Кликает по кнопке 'Войти'"""
        return self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def click_register_link(self):
        """Кликает по ссылке 'Зарегистрироваться'"""
        return self.click_element(LoginPageLocators.REGISTER_LINK)
    
    def click_forgot_password_link(self):
        """Кликает по ссылке 'Восстановить пароль'"""
        return self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    def login(self, email, password):
        """Выполняет вход в систему"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()