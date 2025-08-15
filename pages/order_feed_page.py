import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support import expected_conditions as EC

class OrderFeedPage(BasePage):
    """Page Object для ленты заказов"""
    
    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_total_orders(self):
        """Получает значение счетчика 'Выполнено за всё время'"""
        text = self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        try:
            return int(text)
        except (ValueError, TypeError):
            return 0
    
    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_orders(self):
        """Получает значение счетчика 'Выполнено за сегодня'"""
        try:
            self.wait_for_element_visibility(OrderFeedPageLocators.TODAY_ORDERS)
            text = self.get_text(OrderFeedPageLocators.TODAY_ORDERS)
            return int(text)
        except (ValueError, TypeError):
            return 0
    
    @allure.step("Нажатие на первый заказ в ленте")
    def click_order_item(self):
        """Кликает по первому заказу в ленте"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_ITEM)
        self.click_element(OrderFeedPageLocators.ORDER_ITEM)
    
    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        """Закрывает модальное окно заказа"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_MODAL_CLOSE_BUTTON)
        self.click_element(OrderFeedPageLocators.ORDER_MODAL_CLOSE_BUTTON)
    
    @allure.step("Проверка, что модальное окно заказа видимо")
    def is_order_modal_visible(self):
        """Проверяет, что модальное окно заказа видимо"""
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step("Проверка валидности заголовка модального окна заказа")
    def is_order_modal_title_valid(self):
        """Проверяет, что заголовок модального окна содержит номер заказа"""
        try:
            title = self.get_text(OrderFeedPageLocators.ORDER_MODAL_TITLE)
            return title.startswith("#") and len(title) > 1
        except:
            return False
    
    @allure.step("Получение номеров заказов в работе")
    def get_order_numbers_in_progress(self):
        """Получает номера заказов в работе"""
        try:
            self.wait_for_element_visibility(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
            elements = self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS)
            return [el.text.strip('#') for el in elements]
        except:
            return []
    
    @allure.step("Нажатие кнопки 'Лента заказов'")
    def click_order_feed_button(self):
        """Кликает по кнопке 'Лента заказов'"""
        self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_FEED_BUTTON)
        self.click_element(OrderFeedPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Проверка видимости заказа в ленте")
    def is_order_visible_in_feed(self, order_number):
        """Проверяет, что заказ с указанным номером видим в ленте"""
        try:
            # Ожидаем появления заказа в ленте
            self.wait_for_order_in_feed(order_number, timeout=5)
            return True
        except:
            return False

    @allure.step("Ожидание появления заказа в ленте")
    def wait_for_order_in_feed(self, order_number, timeout=5):
        """Ожидает появления заказа в ленте"""
        return self.wait.until(
            EC.text_to_be_present_in_element(
                OrderFeedPageLocators.ORDERS_LIST, 
                order_number
            ),
            message=f"Заказ {order_number} не появился в ленте за {timeout} секунд"
        )
    
    @allure.step("Проверка увеличения счетчика выполненных заказов")
    def total_orders_counter_increased(self):
        """Проверяет, что счетчик выполненных заказов увеличился"""
        try:
            initial_value = getattr(self, 'initial_total_orders', 0)
            current_value = self.get_total_orders()
            return current_value > initial_value
        except Exception as e:
            print(f"Ошибка при проверке увеличения счетчика выполненных заказов: {str(e)}")
            return False

    @allure.step("Проверка увеличения счетчика заказов за сегодня")
    def today_orders_counter_increased(self):
        """Проверяет, что счетчик заказов за сегодня увеличился"""
        try:
            initial_value = getattr(self, 'initial_today_orders', 0)
            current_value = self.get_today_orders()
            return current_value > initial_value
        except Exception as e:
            print(f"Ошибка при проверке увеличения счетчика заказов за сегодня: {str(e)}")
            return False
    
    @allure.step("Проверка наличия заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        """Проверяет, что заказ находится в разделе 'В работе'"""
        try:
            # Ожидаем появления заказа в разделе "В работе"
            self.wait_for_order_in_progress(order_number, timeout=5)
            return True
        except:
            return False

    @allure.step("Ожидание появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=5):
        """Ожидает появления заказа в разделе 'В работе'"""
        return self.wait.until(
            EC.text_to_be_present_in_element(
                OrderFeedPageLocators.ORDERS_IN_PROGRESS, 
                order_number
            ),
            message=f"Заказ {order_number} не появился в разделе 'В работе' за {timeout} секунд"
        )
    
    @allure.step("Проверка загрузки ленты заказов")
    def is_order_feed_loaded(self):
        """Проверяет, что лента заказов загружена"""
        try:
            self.wait_for_element_visibility(OrderFeedPageLocators.ORDER_ITEM, time=1)
            return True
        except:
            return False