import allure
import pytest
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException

@allure.feature('Основной функционал')
class TestMainFunctionality:
    
    @allure.story('Навигация')
    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, main_page):
        """
        Проверяет переход по клику на «Конструктор»
        """
        main_page.click_constructor_button()
        
        # Проверяем, что URL содержит /constructor
        assert "/constructor" in main_page.get_current_url() or main_page.get_current_url() == "https://stellarburgers.nomoreparties.site/"
    
    @allure.story('Навигация')
    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, main_page):
        """
        Проверяет переход по клику на «Лента заказов»
        """
        main_page.click_order_feed_button()
        
        # Проверяем, что URL содержит /feed
        assert "/feed" in main_page.get_current_url()
    
    @allure.story('Работа с ингредиентами')
    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_shows_details(self, main_page):
        """
        Проверяет, что при клике на ингредиент
        появляется всплывающее окно с деталями
        """
        try:
            main_page.click_bun_item()
            
            # Проверяем, что модальное окно открыто
            assert main_page.is_modal_visible()
            # Проверяем заголовок модального окна
            assert "Детали" in main_page.driver.page_source
        finally:
            # Закрываем модальное окно, если оно открыто
            if main_page.is_modal_visible():
                main_page.close_modal()
                main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
    
    @allure.story('Работа с ингредиентами')
    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_modal_closes_with_close_button(self, main_page):
        """
        Проверяет, что всплывающее окно закрывается
        кликом по крестику
        """
        try:
            main_page.click_bun_item()
            
            # Проверяем, что модальное окно открыто
            assert main_page.is_modal_visible()
            
            # Закрываем модальное окно
            main_page.close_modal()
            
            # Проверяем, что модальное окно закрыто
            assert main_page.is_modal_closed()
        finally:
            # Убедимся, что модальное окно закрыто
            if main_page.is_modal_visible():
                main_page.close_modal()
                main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
    
    @allure.story('Работа с ингредиентами')
    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter_increases(self, main_page):
        """
        Проверяет, что при добавлении ингредиента в заказ,
        увеличивается каунтер данного ингредиента
        """
        try:
            # Получаем начальное значение счетчика для булки
            try:
                initial_counter = int(main_page.get_bun_counter())
            except (ValueError, TypeError):
                initial_counter = 0
            
            # Добавляем булку в заказ
            main_page.click_bun_item()
            main_page.close_modal()
            main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
            
            # Получаем новое значение счетчика
            try:
                new_counter = int(main_page.get_bun_counter())
            except (ValueError, TypeError):
                new_counter = 0
            
            # Проверяем, что счетчик увеличился
            assert new_counter > initial_counter
        finally:
            # Убедимся, что модальное окно закрыто
            if main_page.is_modal_visible():
                main_page.close_modal()
                main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
    
    @allure.story('Оформление заказа')
    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, main_page, login_page, registered_user):
        """
        Проверяет, что залогиненный пользователь может оформить заказ
        """
        # Логинимся
        main_page.click_login_button()
        
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        # Добавляем ингредиенты
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
        main_page.click_sauce_item()
        main_page.close_modal()
        main_page.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
        
        # Оформляем заказ
        main_page.click_order_button()
        
        # Проверяем, что появилось сообщение об успешном оформлении заказа
        try:
            main_page.wait_for_element_visibility(MainPageLocators.ORDER_CONFIRMATION_NUMBER, time=20)
            assert "идентификатор" in main_page.driver.page_source
            assert "Ваш заказ начали готовить" in main_page.driver.page_source
        except TimeoutException:
            pytest.fail("Не появилось сообщение об успешном оформлении заказа")