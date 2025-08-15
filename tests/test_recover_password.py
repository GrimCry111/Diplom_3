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
        # ДЕЙСТВИЕ: Вводим email
        forgot_password_page.enter_email(registered_user["email"])
        
        # ДЕЙСТВИЕ: Нажимаем кнопку "Восстановить"
        forgot_password_page.click_restore_button()
        
        # ПРОВЕРКА: Убеждаемся, что мы на странице ввода пароля
        assert main_page.is_on_reset_password_page(), "Не перешли на страницу ввода пароля"
        
        # ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА: Убеждаемся, что URL содержит /reset-password
        assert "/reset-password" in main_page.get_current_url(), "URL не содержит /reset-password"

    @allure.story('Работа с полем пароля')
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button_activates_password_field(self, reset_password_page):
        """
        Проверяет, что клик по кнопке показать/скрыть пароль
        делает поле активным — подсвечивает его
        """
        # ПРОВЕРКА: Убеждаемся, что поле пароля не активно изначально
        assert not reset_password_page.is_password_field_active(), "Поле пароля активно до клика на кнопку 'глаз'"
        
        # ДЕЙСТВИЕ: Нажимаем на кнопку "глаз"
        reset_password_page.click_eye_button()
        
        # ПРОВЕРКА: Убеждаемся, что поле пароля стало активным
        assert reset_password_page.is_password_field_active(), "Поле пароля не активировалось после клика на кнопку 'глаз'"
        
        # ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА: Убеждаемся, что тип поля изменился с 'password' на 'text'
        assert reset_password_page.get_password_field_type() == "text", "Тип поля не изменился на 'text' после клика"