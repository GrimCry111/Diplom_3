import allure

@allure.feature('Восстановление пароля')
class TestRecoverPassword:
    
    @allure.story('Переход на страницу восстановления пароля')
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password_page(self, main_page, login_page):
        """
        Проверяет переход на страницу восстановления пароля
        по кнопке «Восстановить пароль»
        """
        main_page.click_login_button()
        login_page.click_forgot_password_link()
        
        # Проверяем, что мы на странице восстановления пароля
        assert "Восстановление пароля" in main_page.driver.title
    
    @allure.story('Ввод данных для восстановления')
    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_restore(self, main_page, login_page, forgot_password_page, registered_user):
        """
        Проверяет ввод почты и клик по кнопке «Восстановить»
        """
        main_page.click_login_button()
        login_page.click_forgot_password_link()
        
        forgot_password_page.enter_email(registered_user["email"])
        forgot_password_page.click_restore_button()
        
        # Проверяем, что отображается поле ввода пароля
        assert forgot_password_page.is_password_field_active()
    
    @allure.story('Работа с полем пароля')
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button_activates_password_field(self, main_page, login_page, forgot_password_page, registered_user):
        """
        Проверяет, что клик по кнопке показать/скрыть пароль
        делает поле активным — подсвечивает его
        """
        main_page.click_login_button()
        login_page.click_forgot_password_link()
        
        forgot_password_page.enter_email(registered_user["email"])
        forgot_password_page.click_restore_button()
        
        # Проверяем, что поле пароля не активно изначально
        assert not forgot_password_page.is_password_field_active()
        
        # Нажимаем на кнопку "глаз"
        forgot_password_page.click_eye_button()
        
        # Проверяем, что поле пароля стало активным
        assert forgot_password_page.is_password_field_active()