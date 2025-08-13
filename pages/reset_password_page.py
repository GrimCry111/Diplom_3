import allure
from .base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    """Page Object для страницы сброса пароля"""
    
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """Вводит пароль в поле"""
        self.wait_for_element_visibility(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.send_keys(ResetPasswordPageLocators.PASSWORD_INPUT, password)
        return True
    
    @allure.step("Нажатие кнопки 'глаз'")
    def click_eye_button(self):
        """Кликает по кнопке 'глаз'"""
        try:
            self.wait_for_element_visibility(ResetPasswordPageLocators.EYE_BUTTON)
            self.wait_for_element_to_be_clickable(ResetPasswordPageLocators.EYE_BUTTON)
            
            # Кликаем через JavaScript для надежности
            eye_button = self.find_element(ResetPasswordPageLocators.EYE_BUTTON)
            self.driver.execute_script("arguments[0].click();", eye_button)
                
            return True
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'глаз': {str(e)}")
            return False
    
    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        """Проверяет, активно ли поле пароля (показывает ли пароль в открытом виде)"""
        try:
            password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
            field_type = password_field.get_attribute("type")
            # Если тип поля "text", значит пароль виден (активное состояние)
            return field_type == "text"
        except Exception as e:
            print(f"Ошибка при проверке активности поля пароля: {str(e)}")
            return False