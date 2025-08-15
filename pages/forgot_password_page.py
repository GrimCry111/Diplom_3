import allure
from .base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from urls import RESET_PASSWORD_URL
from selenium.common.exceptions import TimeoutException

class ForgotPasswordPage(BasePage):
    """Page Object для страницы восстановления пароля"""
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        """Вводит email в поле"""
        # Проверяем, видимо ли поле
        if not self.is_element_visible(ForgotPasswordPageLocators.EMAIL_INPUT):
            self.scroll_to_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        
        # Вводим email
        self.wait_for_element_visibility(ForgotPasswordPageLocators.EMAIL_INPUT)
        self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Нажатие кнопки 'Восстановить'")
    def click_restore_button(self):
        """Кликает по кнопке 'Восстановить'"""
        self.wait_for_element_visibility(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.wait_for_element_to_be_clickable(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
        
        # Ожидаем перехода на страницу сброса пароля
        try:
            self.wait_for_url_contains("/reset-password", timeout=10)
        except TimeoutException:
            # Проверяем текущий URL для диагностики ошибки
            current_url = self.get_current_url()
            raise AssertionError(
                f"Не перешли на страницу сброса пароля. Текущий URL: {current_url}"
            )
    
    @allure.step("Нажатие кнопки 'глаз'")
    def click_eye_button(self):
        """Кликает по кнопке 'глаз'"""
        # Убедимся, что мы на правильной странице
        if not self.is_on_reset_password_page():
            current_url = self.get_current_url()
            raise AssertionError(
                f"Не на странице сброса пароля. Текущий URL: {current_url}"
            )
        
        # Ожидаем видимости и кликабельности кнопки
        self.wait_for_element_visibility(ForgotPasswordPageLocators.EYE_BUTTON)
        self.wait_for_element_to_be_clickable(ForgotPasswordPageLocators.EYE_BUTTON)
        
        # Кликаем по кнопке
        try:
            self.click_element(ForgotPasswordPageLocators.EYE_BUTTON)
        except Exception as e:
            # Если обычный клик не сработал, пробуем через JavaScript
            eye_button = self.find_element(ForgotPasswordPageLocators.EYE_BUTTON)
            self.driver.execute_script("arguments[0].click();", eye_button)
        
        # Ожидаем, что поле пароля станет активным
        self.wait_for_password_field_to_become_active()
    
    @allure.step("Ожидание активности поля пароля")
    def wait_for_password_field_to_become_active(self, timeout=10):
        """Ожидает, что поле пароля станет активным (показывает пароль)"""
        try:
            self.wait.until(
                lambda d: self.get_password_field_type() == "text",
                message=f"Поле пароля не стало активным за {timeout} секунд"
            )
        except Exception as e:
            current_type = self.get_password_field_type()
            raise AssertionError(
                f"Поле пароля не стало активным. Текущий тип: {current_type}. Ошибка: {str(e)}"
            )
    
    @allure.step("Получение типа поля пароля")
    def get_password_field_type(self):
        """Возвращает тип поля пароля (password или text)"""
        password_field = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("type")
    
    @allure.step("Проверка, что мы на странице сброса пароля")
    def is_on_reset_password_page(self):
        """Проверяет, что текущая страница - страница сброса пароля"""
        return RESET_PASSWORD_URL in self.get_current_url()