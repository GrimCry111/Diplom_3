import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    """Page Object для ленты заказов"""
    
    @allure.step("Получение значения счетчика 'Выполнено за все время'")
    def get_total_orders(self):
        """Получает значение счетчика 'Выполнено за все время'"""
        self.wait_for_element_visibility(OrderFeedPageLocators.TOTAL_ORDERS)
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS))
    
    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_orders(self):
        """Получает значение счетчика 'Выполнено за сегодня'"""
        self.wait_for_element_visibility(OrderFeedPageLocators.TODAY_ORDERS)
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS))
    
    @allure.step("Нажатие на первый заказ в ленте")
    def click_order_item(self):
        """Кликает по первому заказу в ленте"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_ITEM)
        return self.click_element(OrderFeedPageLocators.ORDER_ITEM)
    
    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        """Закрывает модальное окно заказа"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_MODAL_CLOSE_BUTTON)
        return self.click_element(OrderFeedPageLocators.ORDER_MODAL_CLOSE_BUTTON)
    
    @allure.step("Проверка видимости модального окна заказа")
    def is_order_modal_visible(self):
        """Проверяет видимость модального окна заказа"""
        try:
            self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_MODAL, time=5)
            return True
        except:
            return False
    
    @allure.step("Получение номеров заказов в работе")
    def get_order_numbers_in_progress(self):
        """Получает номера заказов в работе"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        elements = self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        return [el.text.strip('#') for el in elements]
    
    @allure.step("Нажатие кнопки 'Лента заказов'")
    def click_order_feed_button(self):
        """Кликает по кнопке 'Лента заказов'"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_FEED_BUTTON)
        return self.click_element(OrderFeedPageLocators.ORDER_FEED_BUTTON)