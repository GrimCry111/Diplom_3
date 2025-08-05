import allure

@allure.feature('Лента заказов')
class TestOrderFeed:
    
    @allure.story('Просмотр деталей заказа')
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_shows_details(self, main_page, order_feed_page):
        """
        Проверяет, что при клике на заказ
        открывается всплывающее окно с деталями
        """
        main_page.click_order_feed_button()
        
        order_feed_page.click_order_item()
        
        # Проверяем, что модальное окно заказа открыто
        assert order_feed_page.is_order_modal_visible()
        # Проверяем, что заголовок модального окна содержит номер заказа
        assert order_feed_page.get_text(order_feed_page.ORDER_MODAL_TITLE).startswith("#")
    
    @allure.story('Синхронизация заказов')
    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_appear_in_order_feed(self, main_page, login_page, profile_page, order_feed_page, registered_user):
        """
        Проверяет, что заказы пользователя из раздела «История заказов»
        отображаются на странице «Лента заказов»
        """
        # Создаем заказ
        main_page.click_login_button()
        
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.click_order_button()
        
        # Получаем номер заказа
        order_number = main_page.get_order_number()
        
        # Переходим в ленту заказов
        main_page.click_order_feed_button()
        
        # Проверяем, что заказ пользователя отображается в ленте
        order_numbers = order_feed_page.get_order_numbers_in_progress()
        assert order_number in order_numbers
    
    @allure.story('Счетчики заказов')
    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_orders_counter_increases(self, main_page, login_page, registered_user):
        """
        Проверяет, что при создании нового заказа
        счётчик "Выполнено за всё время" увеличивается
        """
        # Получаем начальное значение счетчика
        main_page.click_order_feed_button()
        initial_total = main_page.get_total_orders()
        
        # Создаем заказ
        main_page.open()
        main_page.click_login_button()
        
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.click_order_button()
        
        # Получаем новое значение счетчика
        main_page.click_order_feed_button()
        new_total = main_page.get_total_orders()
        
        # Проверяем, что счетчик увеличился
        assert new_total == initial_total + 1
    
    @allure.story('Счетчики заказов')
    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_orders_counter_increases(self, main_page, login_page, registered_user):
        """
        Проверяет, что при создании нового заказа
        счётчик "Выполнено за сегодня" увеличивается
        """
        # Получаем начальное значение счетчика
        main_page.click_order_feed_button()
        initial_today = main_page.get_today_orders()
        
        # Создаем заказ
        main_page.open()
        main_page.click_login_button()
        
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.click_order_button()
        
        # Получаем новое значение счетчика
        main_page.click_order_feed_button()
        new_today = main_page.get_today_orders()
        
        # Проверяем, что счетчик увеличился
        assert new_today == initial_today + 1
    
    @allure.story('Статус заказа')
    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_progress(self, main_page, login_page, registered_user):
        """
        Проверяет, что после оформления заказа
        его номер появляется в разделе "В работе"
        """
        # Создаем заказ
        main_page.click_login_button()
        
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
        
        main_page.click_bun_item()
        main_page.close_modal()
        main_page.click_order_button()
        
        # Получаем номер заказа
        order_number = main_page.get_order_number()
        
        # Переходим в ленту заказов
        main_page.click_order_feed_button()
        
        # Проверяем, что заказ появился в разделе "В работе"
        order_numbers = main_page.get_order_numbers_in_progress()
        assert order_number in order_numbers