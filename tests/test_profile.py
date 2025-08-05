import allure
import pytest

@allure.feature('Личный кабинет')
class TestProfile:
    
    @allure.story('Навигация по личному кабинету')
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_profile(self, main_page, login_page, registered_user):
        """
        Проверяет переход по клику на «Личный кабинет»
        """
        # Логинимся
        main_page.click_login_button()
        
        login_page.enter_email("email@test.com")
        login_page.enter_password("password")
        login_page.click_login_button()
        
        # Переходим в личный кабинет
        main_page.click_profile_button()
        main_page.close_warning_popup()
        
        # Проверяем, что мы в личном кабинете
        assert "Профиль" in main_page.driver.title or "Личный кабинет" in main_page.driver.page_source
    
    @allure.story('Навигация по личному кабинету')
    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, main_page, login_page, profile_page, registered_user):
        """
        Проверяет переход в раздел «История заказов»
        """
        # Логинимся
        main_page.click_login_button()
        
        login_page.enter_email("email@test.com")
        login_page.enter_password("password")
        login_page.click_login_button()
        
        # Переходим в профиль
        main_page.click_profile_button()
        main_page.close_warning_popup()
        
        # Переходим в историю заказов
        profile_page.click_order_history_link()
        
        # Проверяем, что мы в истории заказов
        assert "История заказов" in main_page.driver.title or "История заказов" in main_page.driver.page_source
    
    @allure.story('Выход из аккаунта')
    @allure.title('Выход из аккаунта')
    def test_logout(self, main_page, login_page, profile_page, registered_user):
        """
        Проверяет выход из аккаунта
        """
        # Логинимся
        main_page.click_login_button()
        
        login_page.enter_email("email@test.com")
        login_page.enter_password("password")
        login_page.click_login_button()
        
        # Переходим в профиль
        main_page.click_profile_button()
        main_page.close_warning_popup()

        
        # Выходим из аккаунта
        profile_page.click_logout_button()
        
        # Проверяем, что мы вернулись на главную страницу
        assert main_page.get_current_url() == "https://stellarburgers.nomoreparties.site/"