import allure
from .base_page import BasePage
from urls import RESET_PASSWORD_URL
from locators.reset_password_page_locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    """Page Object для страницы сброса пароля"""
    
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """Вводит пароль в поле"""
        # Сначала убедимся, что мы на нужной странице
        if not self.is_on_reset_password_page():
            raise AssertionError("Не на странице сброса пароля")
        
        # Закрываем модальное окно, если оно есть
        self.close_modal_if_present()
        
        # Вводим пароль
        self.wait_for_element_visibility(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.send_keys(ResetPasswordPageLocators.PASSWORD_INPUT, password)
    
    @allure.step("Нажатие кнопки 'глаз'")
    def click_eye_button(self):
        """Кликает по кнопке 'глаз'"""
        # Убедимся, что мы на нужной странице
        if not self.is_on_reset_password_page():
            raise AssertionError("Не на странице сброса пароля")
        
        # Закрываем модальное окно, если оно есть
        self.close_modal_if_present()
        
        # Ожидаем видимости и кликабельности кнопки
        self.wait_for_element_visibility(ResetPasswordPageLocators.EYE_BUTTON)
        self.wait_for_element_to_be_clickable(ResetPasswordPageLocators.EYE_BUTTON)
        
        # Кликаем по кнопке
        self.click_element(ResetPasswordPageLocators.EYE_BUTTON)
        
        # Ожидаем, что поле пароля станет активным
        self.wait_for_password_field_to_become_active()
    
    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        """Проверяет, активно ли поле пароля (показывает ли пароль в открытом виде)"""
        try:
            # Убедимся, что мы на нужной странице
            if not self.is_on_reset_password_page():
                return False
            
            password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
            field_type = password_field.get_attribute("type")
            return field_type == "text"
        except:
            return False

    @allure.step("Получение типа поля пароля")
    def get_password_field_type(self):
        """Возвращает тип поля пароля (password или text)"""
        try:
            password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
            return password_field.get_attribute("type")
        except:
            return None
        
    @allure.step("Ожидание видимости поля пароля")
    def wait_for_password_field_to_be_visible(self, timeout=10):
        """Ожидает появления поля пароля"""
        return self.wait_for_element_visibility(ResetPasswordPageLocators.PASSWORD_INPUT, time=timeout)
    
    @allure.step("Ожидание активности поля пароля")
    def wait_for_password_field_to_become_active(self, timeout=5):
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
    
    @allure.step("Проверка, что мы на странице сброса пароля")
    def is_on_reset_password_page(self):
        """Проверяет, что текущая страница - страница сброса пароля"""
        
        return RESET_PASSWORD_URL in self.get_current_url()