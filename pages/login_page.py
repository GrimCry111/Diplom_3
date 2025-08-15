import allure
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .main_page import MainPage
from urls import LOGIN_URL

class LoginPage(BasePage):
    """Page Object для страницы входа"""
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        """Вводит email в поле"""
        self.wait_for_element_visibility(LoginPageLocators.EMAIL_INPUT)
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        # УДАЛИТЬ: return True
    
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """Вводит пароль в поле"""
        self.wait_for_element_visibility(LoginPageLocators.PASSWORD_INPUT)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        # УДАЛИТЬ: return True
    
    @allure.step("Нажатие кнопки 'Войти'")
    def click_login_button(self):
        """Кликает по кнопке 'Войти'"""
        self.wait_for_element_visibility(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        
        try:
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
        except Exception as e:
            # Если обычный клик не сработал, используем JavaScript
            login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
            self.driver.execute_script("arguments[0].click();", login_button)
    
    @allure.step("Переход по ссылке 'Зарегистрироваться'")
    def click_register_link(self):
        """Кликает по ссылке 'Зарегистрироваться'"""
        self.wait_for_element_visibility(LoginPageLocators.REGISTER_LINK)
        self.wait_for_element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        self.click_element(LoginPageLocators.REGISTER_LINK)
        # УДАЛИТЬ: return
    
    @allure.step("Нажатие на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        """Кликает по ссылке 'Восстановить пароль'"""
        # Закрываем модальное окно, если оно есть
        main_page = MainPage(self.driver)
        main_page.close_modal_if_present()
        
        # Ожидаем появления ссылки
        self.wait_for_element_visibility(LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.wait_for_element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        
        # Прокручиваем к элементу
        self.scroll_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        
        # Кликаем по ссылке
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Выполнение входа в систему")
    def login(self, email, password):
        """Выполняет вход в систему"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()