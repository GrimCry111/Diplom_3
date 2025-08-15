import allure

@allure.feature('Основной функционал')
class TestMainFunctionality:
    
    @allure.story('Навигация')
    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, main_page):
        """
        Проверяет переход по клику на «Конструктор»
        """
        main_page.click_constructor_button()
        
        # Проверяем, что мы на странице конструктора
        assert main_page.is_on_constructor_page()
    
    @allure.story('Навигация')
    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, main_page):
        """
        Проверяет переход по клику на «Лента заказов»
        """
        main_page.click_order_feed_button()
        
        # Проверяем, что мы на странице ленты заказов
        assert main_page.is_on_order_feed_page()
    
    @allure.story('Работа с ингредиентами')
    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_shows_details(self, main_page):
        """
        Проверяет, что при клике на ингредиент
        появляется всплывающее окно с деталями
        """
        main_page.click_bun_item()
        
        # Проверяем, что модальное окно открыто
        assert main_page.is_modal_visible()
        
        # Проверяем, что заголовок модального окна содержит "Детали"
        assert main_page.is_modal_title_contains("Детали")
    
    @allure.story('Работа с ингредиентами')
    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_modal_closes_with_close_button(self, main_page):
        """
        Проверяет, что всплывающее окно закрывается
        кликом по крестику
        """
        # Открываем модальное окно
        main_page.click_bun_item()
        
        # Проверяем, что модальное окно открыто
        assert main_page.is_modal_visible()
        
        # Закрываем модальное окно
        main_page.close_modal()
        
        # Проверяем, что модальное окно закрыто
        assert main_page.is_modal_closed()
    
    @allure.story('Работа с ингредиентами')
    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter_increases(self, main_page):
        """
        Проверяет, что при добавлении ингредиента в заказ,
        увеличивается каунтер данного ингредиента
        """
        # Получаем начальное значение счетчика для булки
        initial_counter = main_page.get_bun_counter_value()
        
        # Добавляем булку в заказ
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.wait_for_modal_to_close()
        
        # Получаем новое значение счетчика
        new_counter = main_page.get_bun_counter_value()
        
        # Проверяем, что счетчик увеличился
        assert new_counter == initial_counter + 1
    
    @allure.story('Оформление заказа')
    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, main_page, login_page, registered_user,profile_page):
        """
        Проверяет, что залогиненный пользователь может оформить заказ
        """
        # Логинимся
        main_page.click_login_button()
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        # Проверяем, что пользователь авторизован
        assert main_page.is_user_logged_in(), "Пользователь не авторизован"
        
        # Добавляем ингредиенты
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.wait_for_modal_to_close()
        main_page.click_sauce_item()
        main_page.close_modal()
        main_page.wait_for_modal_to_close()
        
        # Оформляем заказ
        main_page.click_order_button()
        
        order_number = main_page.get_order_number()

        # Переходим в историю заказов
        main_page.click_profile_button()
        profile_page.click_order_history_link()

        # Проверяем, что заказ есть в истории
        assert profile_page.is_order_in_history(order_number), f"Заказ {order_number} не найден в истории заказов"