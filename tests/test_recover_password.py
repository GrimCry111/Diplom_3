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
        # Закрываем модальное окно, если оно есть
        main_page.close_modal_if_present()
        
        # Переходим на страницу входа
        main_page.click_login_button()
        
        # Нажимаем на ссылку "Восстановить пароль"
        login_page.click_forgot_password_link()
        
        # Проверяем, что мы на странице восстановления пароля

        assert main_page.is_on_forgot_password_page(), "Не перешли на страницу восстановления пароля"
    @allure.story('Ввод данных для восстановления')
    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_restore(self, forgot_password_page, registered_user, main_page):
        """
        Проверяет ввод почты и клик по кнопке «Восстановить»
        """
        # Вводим email
        assert forgot_password_page.enter_email(registered_user["email"]), "Не удалось ввести email"
        
        # Нажимаем кнопку "Восстановить"
        assert forgot_password_page.click_restore_button(), "Не удалось нажать кнопку 'Восстановить'"
        
        # Проверяем, что мы на странице ввода пароля
        assert main_page.is_on_reset_password_page(), "Не перешли на страницу ввода пароля"
    
    @allure.story('Работа с полем пароля')
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button_activates_password_field(self, forgot_password_page, registered_user, main_page, reset_password_page):
        """
        Проверяет, что клик по кнопке показать/скрыть пароль
        делает поле активным — подсвечивает его
        """
        # Вводим email
        assert forgot_password_page.enter_email(registered_user["email"]), "Не удалось ввести email"
        
        # Нажимаем кнопку "Восстановить"
        assert forgot_password_page.click_restore_button(), "Не удалось нажать кнопку 'Восстановить'"
        
        # Проверяем, что мы на странице ввода пароля
        assert main_page.is_on_reset_password_page(), "Не перешли на страницу ввода пароля"
        
        # Проверяем, что поле пароля не активно изначально
        assert not reset_password_page.is_password_field_active(), "Поле пароля активно до клика на кнопку 'глаз'"
        
        # Нажимаем на кнопку "глаз"
        assert reset_password_page.click_eye_button(), "Не удалось нажать кнопку 'глаз'"
        
        # Проверяем, что поле пароля стало активным
        assert reset_password_page.is_password_field_active(), "Поле пароля не активировалось после клика на кнопку 'глаз'"