from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Page Object для главной страницы"""
    
    def click_login_button(self):
        """Кликает по кнопке 'Войти в аккаунт'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.LOGIN_BUTTON)
            return self.click_element(MainPageLocators.LOGIN_BUTTON)
        except:
            pass
    
    def click_constructor_button(self):
        """Кликает по кнопке 'Конструктор'"""
        self.wait_for_element_visibility(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Кликает по логотипу"""
        self.wait_for_element_visibility(MainPageLocators.LOGO_BUTTON)
        return self.click_element(MainPageLocators.LOGO_BUTTON)
    
    def click_buns_section(self):
        """Кликает по секции 'Булки'"""
        self.wait_for_element_visibility(MainPageLocators.BUNS_SECTION)
        return self.click_element(MainPageLocators.BUNS_SECTION)
    
    def click_sauces_section(self):
        """Кликает по секции 'Соусы'"""
        self.wait_for_element_visibility(MainPageLocators.SAUCES_SECTION)
        return self.click_element(MainPageLocators.SAUCES_SECTION)
    
    def click_fillings_section(self):
        """Кликает по секции 'Начинки'"""
        self.wait_for_element_visibility(MainPageLocators.FILLINGS_SECTION)
        return self.click_element(MainPageLocators.FILLINGS_SECTION)
    
    def click_bun_item(self):
        """Кликает по булке"""
        self.wait_for_element_visibility(MainPageLocators.BUN_ITEM)
        return self.click_element(MainPageLocators.BUN_ITEM)
    
    def click_sauce_item(self):
        """Кликает по соусу"""
        self.wait_for_element_visibility(MainPageLocators.SAUCE_ITEM)
        return self.click_element(MainPageLocators.SAUCE_ITEM)
    
    def click_filling_item(self):
        """Кликает по начинке"""
        self.wait_for_element_visibility(MainPageLocators.FILLING_ITEM)
        return self.click_element(MainPageLocators.FILLING_ITEM)
    
    def click_order_button(self):
        """Кликает по кнопке 'Оформить заказ'"""
        self.wait_for_element_visibility(MainPageLocators.ORDER_BUTTON)
        return self.click_element(MainPageLocators.ORDER_BUTTON)
    
    def click_order_feed_button(self):
        """Кликает по кнопке 'Лента заказов'"""
        self.wait_for_element_visibility(MainPageLocators.ORDER_FEED_BUTTON)
        return self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    def click_profile_button(self):
        """Кликает по кнопке 'Личный кабинет'"""
        self.wait_for_element_visibility(MainPageLocators.PROFILE_BUTTON)
        return self.click_element(MainPageLocators.PROFILE_BUTTON)
    
    def close_modal(self):
        """Закрывает модальное окно"""
        self.wait_for_element_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
        return self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    def is_modal_visible(self):
        """Проверяет видимость модального окна"""
        try:
            self.wait_for_element_visibility(MainPageLocators.MODAL_WINDOW, time=5)
            return True
        except:
            return False
    
    def is_modal_closed(self):
        """Проверяет, что модальное окно закрыто"""
        try:
            self.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW, time=5)
            return True
        except:
            return False
    
    def get_bun_counter(self):
        """Получает значение счетчика булок"""
        self.wait_for_element_visibility(MainPageLocators.BUN_COUNTER)
        return self.get_text(MainPageLocators.BUN_COUNTER)
    
    def get_sauce_counter(self):
        """Получает значение счетчика соусов"""
        self.wait_for_element_visibility(MainPageLocators.SAUCE_COUNTER)
        return self.get_text(MainPageLocators.SAUCE_COUNTER)
    
    def get_filling_counter(self):
        """Получает значение счетчика начинок"""
        self.wait_for_element_visibility(MainPageLocators.FILLING_COUNTER)
        return self.get_text(MainPageLocators.FILLING_COUNTER)
    
    def get_order_number(self):
        """Получает номер заказа после оформления"""
        try:
            self.wait_for_element_visibility(MainPageLocators.ORDER_CONFIRMATION_NUMBER, time=10)
            return self.get_text(MainPageLocators.ORDER_CONFIRMATION_NUMBER).strip('#')
        except:
            # Попробуем найти номер заказа другим способом
            try:
                order_number_element = self.find_element((By.XPATH, "//p[contains(@class, 'text')]"), time=5)
                return order_number_element.text.strip('#')
            except:
                return None
    
    def is_order_confirmation_visible(self):
        """Проверяет видимость подтверждения заказа"""
        try:
            self.wait_for_element_visibility(MainPageLocators.ORDER_CONFIRMATION_TITLE, time=5)
            self.wait_for_element_visibility(MainPageLocators.ORDER_CONFIRMATION_TEXT, time=5)
            return True
        except:
            return False
    
    def is_buns_section_active(self):
        """Проверяет, активна ли секция 'Булки'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.BUNS_SECTION_ACTIVE, time=3)
            return True
        except:
            return False
    
    def is_sauces_section_active(self):
        """Проверяет, активна ли секция 'Соусы'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.SAUCES_SECTION_ACTIVE, time=3)
            return True
        except:
            return False
    
    def is_fillings_section_active(self):
        """Проверяет, активна ли секция 'Начинки'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.FILLINGS_SECTION_ACTIVE, time=3)
            return True
        except:
            return False