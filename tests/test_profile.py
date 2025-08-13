import allure
import pytest
from urls import PROFILE_URL, MAIN_PAGE_URL

@allure.feature('Личный кабинет')
class TestProfile:
    
    @allure.story('Навигация по личному кабинету')
    @allure.title('Проверка отображения личного кабинета')
    def test_profile_page_display(self, profile_page, main_page):
        """
        Проверяет, что после авторизации мы видим элементы личного кабинета
        
        Шаги:
        1. Пользователь авторизован через фикстуру profile_page
        2. Проверяем наличие элементов профиля
        """
        # Нажимаем на кнопку "Личный кабинет"
        main_page.click_profile_button()
        # Проверяем, что мы в личном кабинете
        assert main_page.is_on_profile_page()
        assert profile_page.is_profile_fields_visible(), "Поля профиля не отображаются"
        assert profile_page.are_buttons_visible(), "Кнопки 'Сохранить' и 'Отмена' не отображаются"
        
    @allure.story('Навигация по личному кабинету')
    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, main_page, profile_page):
        """
        Проверяет переход в раздел «История заказов»
        
        Шаги:
        1. Пользователь уже залогинен через фикстуру profile_page
        2. Нажимаем на кнопку "Личный кабинет"
        3. Нажимаем на ссылку "История заказов"
        4. Проверяем, что URL содержит путь к истории заказов
        """
        # Пользователь уже залогинен через фикстуру profile_page
        
        # Нажимаем на кнопку "Личный кабинет"
        main_page.click_profile_button()
        
        # Увеличиваем время ожидания для загрузки страницы профиля
        main_page.wait_for_page_load(PROFILE_URL, timeout=25)
        
        # Переходим в историю заказов
        profile_page.click_order_history_link()
        
        # Увеличиваем время ожидания для перехода
        main_page.wait_for_page_load("/account/order-history", timeout=25)
        
        # Проверяем, что мы в истории заказов
        assert main_page.is_on_order_history_page()
    
    @allure.story('Выход из аккаунта')
    @allure.title('Выход из аккаунта')
    def test_logout(self, main_page, profile_page):
        """
        Проверяет выход из аккаунта
        
        Шаги:
        1. Пользователь уже залогинен через фикстуру profile_page
        2. Нажимаем на кнопку "Личный кабинет"
        3. Нажимаем на кнопку "Выход"
        4. Проверяем, что URL содержит путь к главной странице
        """
        # Пользователь уже залогинен через фикстуру profile_page
        
        # Нажимаем на кнопку "Личный кабинет"
        main_page.click_profile_button()
        
        # Увеличиваем время ожидания для загрузки страницы профиля
        main_page.wait_for_page_load(PROFILE_URL, timeout=25)
        
        # Выходим из аккаунта
        profile_page.click_logout_button()
        
        # Увеличиваем время ожидания для перехода
        main_page.wait_for_page_load(MAIN_PAGE_URL, timeout=30)
        
        # Проверяем, что мы вернулись на главную страницу
        assert main_page.is_on_main_page()