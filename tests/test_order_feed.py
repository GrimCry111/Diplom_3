import allure

@allure.feature('Лента заказов')
class TestOrderFeed:
    
    @allure.story('Просмотр деталей заказа')
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_shows_details(self, order_feed_page):
        """
        Проверяет, что при клике на заказ
        открывается всплывающее окно с деталями
        """
        # ДЕЙСТВИЕ: Переходим в ленту заказов
        order_feed_page.open()
        
        # ПРОВЕРКА: Убеждаемся, что лента заказов загружена
        assert order_feed_page.is_order_feed_loaded(), "Лента заказов не загружена"
        
        # ДЕЙСТВИЕ: Кликаем на первый заказ
        order_feed_page.click_order_item()
        
        # ПРОВЕРКА: Убеждаемся, что модальное окно заказа открыто
        assert order_feed_page.is_order_modal_visible(), "Модальное окно заказа не открылось"
        
        # ПРОВЕРКА: Убеждаемся, что заголовок модального окна содержит номер заказа
        assert order_feed_page.is_order_modal_title_valid(), "Неверный формат заголовка модального окна"
    
    @allure.story('Синхронизация заказов')
    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_appear_in_order_feed(self, order_feed_page, placed_order):
        """
        Проверяет, что заказы пользователя из раздела «История заказов»
        отображаются на странице «Лента заказов»
        """
        # ДЕЙСТВИЕ: Получаем номер созданного заказа
        order_number = placed_order["number"]
        
        # ДЕЙСТВИЕ: Переходим в ленту заказов
        order_feed_page.open()
        
        # ПРОВЕРКА: Убеждаемся, что заказ пользователя отображается в ленте
        assert order_feed_page.is_order_visible_in_feed(order_number), f"Заказ {order_number} не найден в ленте заказов"
    
    @allure.story('Счетчики заказов')
    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_orders_counter_increases(self, order_feed_page):
        """
        Проверяет, что при создании нового заказа
        счётчик "Выполнено за всё время" увеличивается
        """
        # ДЕЙСТВИЕ: Переходим в ленту заказов
        order_feed_page.open()
        
        # ПРОВЕРКА: Убеждаемся, что счетчик увеличился
        assert order_feed_page.total_orders_counter_increased(), "Счетчик 'Выполнено за всё время' не увеличился"
    
    @allure.story('Счетчики заказов')
    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_orders_counter_increases(self, order_feed_page):
        """
        Проверяет, что при создании нового заказа
        счётчик "Выполнено за сегодня" увеличивается
        """
        # ДЕЙСТВИЕ: Переходим в ленту заказов
        order_feed_page.open()
        
        # ПРОВЕРКА: Убеждаемся, что счетчик увеличился
        assert order_feed_page.today_orders_counter_increased(), "Счетчик 'Выполнено за сегодня' не увеличился"
    
    @allure.story('Статус заказа')
    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_progress(self, order_feed_page, placed_order):
        """
        Проверяет, что после оформления заказа
        его номер появляется в разделе "В работе"
        """
        # ДЕЙСТВИЕ: Получаем номер заказа
        order_number = placed_order["number"]
        
        # ДЕЙСТВИЕ: Переходим в ленту заказов
        order_feed_page.open()
        
        # ПРОВЕРКА: Убеждаемся, что заказ появился в разделе "В работе"
        assert order_feed_page.is_order_in_progress(order_number), f"Заказ {order_number} не появился в разделе 'В работе'"