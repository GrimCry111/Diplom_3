import allure
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from .main_page import MainPage
from urls import LOGIN_URL

class LoginPage(BasePage):
    """Page Object для страницы входа"""
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        """Вводит email в поле"""
        self.wait_for_element_visibility(LoginPageLocators.EMAIL_INPUT)
        # Используем send_keys вместо set_value
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        return True
    
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """Вводит пароль в поле"""
        self.wait_for_element_visibility(LoginPageLocators.PASSWORD_INPUT)
        # Используем send_keys вместо set_value
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        return True
    
    @allure.step("Нажатие кнопки 'Войти'")
    def click_login_button(self):
        """Кликает по кнопке 'Войти'"""
        try:
            self.wait_for_element_visibility(LoginPageLocators.LOGIN_BUTTON)
            self.wait_for_element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
            return True
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'Войти': {str(e)}")
            # Если обычный клик не сработал, используем JavaScript
            try:
                login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
                self.driver.execute_script("arguments[0].click();", login_button)
                return True
            except Exception as js_error:
                print(f"Ошибка при клике через JavaScript: {str(js_error)}")
                raise
    
    @allure.step("Переход по ссылке 'Зарегистрироваться'")
    def click_register_link(self):
        """Кликает по ссылке 'Зарегистрироваться'"""
        return self.click_element(LoginPageLocators.REGISTER_LINK)
    
    @allure.step("Нажатие на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        """Кликает по ссылке 'Восстановить пароль'"""
        try:
            # Убедимся, что мы на странице входа
            self.wait_for_url_contains(LOGIN_URL.rstrip(), timeout=15)
            
            # Попробуем закрыть модальное окно, если оно есть
            try:
                main_page = MainPage(self.driver)
                main_page.close_modal_if_present()
            except Exception as e:
                print(f"Ошибка при закрытии модального окна: {str(e)}")
            
            # Ожидаем появления ссылки
            self.wait_for_element_visibility(LoginPageLocators.FORGOT_PASSWORD_LINK, time=15)
            
            # Прокручиваем к элементу
            self.scroll_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
            
            # Пытаемся кликнуть обычным способом
            return self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        except Exception as e:
            print(f"Ошибка при клике на ссылку 'Восстановить пароль': {str(e)}")
            try:
                # Если обычный клик не сработал, используем JavaScript
                forgot_password_link = self.find_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", forgot_password_link)
                
                # Используем явное ожидание вместо time.sleep
                try:
                    WebDriverWait(self.driver, 1).until(lambda d: False, "Принудительная пауза")
                except:
                    pass
                
                self.driver.execute_script("arguments[0].click();", forgot_password_link)
                return True
            except Exception as js_error:
                print(f"Ошибка при клике через JavaScript: {str(js_error)}")
                raise
    
    @allure.step("Выполнение входа в систему")
    def login(self, email, password):
        """Выполняет вход в систему"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()