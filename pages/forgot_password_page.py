import allure
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from urls import FORGOT_PASSWORD_URL

from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):
    """Page Object для страницы восстановления пароля"""
    
    def open(self):
        """Не нужно переопределять, так как страница открывается через переходы"""
        return self
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        """Вводит email в поле"""
        try:
            # Сначала убедимся, что мы на нужной странице
            if not self.is_on_forgot_password_page():
                print("Не на странице восстановления пароля, перезагружаем...")
                self.driver.refresh()
                # Ждем, пока страница загрузится
                self.wait_for_url_contains(FORGOT_PASSWORD_URL, timeout=10)
            
            # Проверяем, видимо ли поле
            if not self.is_element_visible(ForgotPasswordPageLocators.EMAIL_INPUT):
                # Прокручиваем к полю
                self.scroll_to_element(ForgotPasswordPageLocators.EMAIL_INPUT)
            
            # Вводим email
            self.wait_for_element_visibility(ForgotPasswordPageLocators.EMAIL_INPUT, time=15)
            self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)
            return True
        except Exception as e:
            print(f"Ошибка при вводе email: {str(e)}")
            # Попробуем через JavaScript
            try:
                email_input = self.find_element(ForgotPasswordPageLocators.EMAIL_INPUT)
                self.driver.execute_script(f"arguments[0].value = '{email}';", email_input)
                return True
            except Exception as js_error:
                print(f"Ошибка при вводе через JavaScript: {str(js_error)}")
                raise   
    
    @allure.step("Нажатие кнопки 'Восстановить'")
    def click_restore_button(self):
        """Кликает по кнопке 'Восстановить'"""
        try:
            self.wait_for_element_visibility(ForgotPasswordPageLocators.RESTORE_BUTTON)
            self.wait_for_element_to_be_clickable(ForgotPasswordPageLocators.RESTORE_BUTTON)
            self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
            
            # Даем время на переход
            try:
                # Используем явное ожидание вместо time.sleep
                WebDriverWait(self.driver, 2).until(
                    EC.url_contains("/reset-password"),
                    "Не перешли на страницу сброса пароля"
                )
            except:
                pass
                
            return True
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'Восстановить': {str(e)}")
            try:
                # Если обычный клик не сработал, используем JavaScript
                restore_button = self.find_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
                self.driver.execute_script("arguments[0].click();", restore_button)
                
                # Даем время на переход
                try:
                    WebDriverWait(self.driver, 2).until(
                        EC.url_contains("/reset-password"),
                        "Не перешли на страницу сброса пароля"
                    )
                except:
                    pass
                    
                return True
            except Exception as js_error:
                print(f"Ошибка при клике через JavaScript: {str(js_error)}")
                raise
    
    @allure.step("Нажатие кнопки 'глаз'")
    def click_eye_button(self):
        """Кликает по кнопке 'глаз'"""
        try:
            # Сначала убедимся, что мы на правильной странице
            if not self.is_on_reset_password_page():
                print("Не на странице сброса пароля, не можем нажать на кнопку 'глаз'")
                return False
                
            self.wait_for_element_visibility(ForgotPasswordPageLocators.EYE_BUTTON)
            self.wait_for_element_to_be_clickable(ForgotPasswordPageLocators.EYE_BUTTON)
            
            # Попробуем разные способы клика
            try:
                # Сначала обычный клик
                self.click_element(ForgotPasswordPageLocators.EYE_BUTTON)
            except:
                # Если не сработало, попробуем через JavaScript
                eye_button = self.find_element(ForgotPasswordPageLocators.EYE_BUTTON)
                self.driver.execute_script("arguments[0].click();", eye_button)
            
            # Даем время для обработки события
            try:
                WebDriverWait(self.driver, 2).until(
                    lambda d: False, 
                    "Принудительная пауза"
                )
            except:
                pass
                
            return True
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'глаз': {str(e)}")
            return False
        
    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        """Проверяет, активно ли поле пароля (показывает ли пароль в открытом виде)"""
        try:
            # Сначала убедимся, что мы на правильной странице
            if not self.is_on_reset_password_page():
                print("Не на странице сброса пароля")
                return False
                
            # Попробуем найти поле пароля разными способами
            try:
                password_field = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
            except:
                # Дополнительная попытка найти поле пароля
                try:
                    password_field = self.find_element((By.XPATH, "//input[contains(@class, 'input__textfield')]"))
                except:
                    print("Не удалось найти поле пароля")
                    return False
            
            # Получаем тип поля
            field_type = password_field.get_attribute("type")
            print(f"Тип поля пароля: {field_type}")
            
            # Если тип поля "text", значит пароль виден (активное состояние)
            return field_type == "text"
        except Exception as e:
            print(f"Ошибка при проверке активности поля пароля: {str(e)}")
            return False