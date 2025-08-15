import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from urls import CONSTRUCTOR_URL, ORDER_FEED_URL, PROFILE_URL, MAIN_PAGE_URL, ORDER_HISTORY_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL

class MainPage(BasePage):
    """Page Object для главной страницы"""
    
    @allure.step("Нажатие на кнопку 'Войти'")
    def click_login_button(self):
        """Кликает по кнопке 'Войти'"""
        # Сначала закрываем модальное окно, если оно есть
        self.close_modal_if_present()
        
        # Увеличиваем время ожидания перед кликом
        self.wait_for_element_visibility(MainPageLocators.LOGIN_BUTTON)
        self.wait_for_element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        
        try:
            # Пытаемся кликнуть обычным способом
            self.click_element(MainPageLocators.LOGIN_BUTTON)
        except (ElementClickInterceptedException, StaleElementReferenceException):
            # Если обычный клик не сработал, используем JavaScript
            login_button = self.find_element(MainPageLocators.LOGIN_BUTTON)
            self.driver.execute_script("arguments[0].click();", login_button)
    
    @allure.step("Нажатие кнопки 'Конструктор'")
    def click_constructor_button(self):
        """Кликает по кнопке 'Конструктор'"""
        self.wait_for_element_visibility(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Нажатие на логотип")
    def click_logo(self):
        """Кликает по логотипу"""
        self.wait_for_element_visibility(MainPageLocators.LOGO_BUTTON)
        self.click_element(MainPageLocators.LOGO_BUTTON)
    
    @allure.step("Нажатие на секцию 'Булки'")
    def click_buns_section(self):
        """Кликает по секции 'Булки'"""
        self.wait_for_element_visibility(MainPageLocators.BUNS_SECTION)
        self.click_element(MainPageLocators.BUNS_SECTION)
    
    @allure.step("Нажатие на секцию 'Соусы'")
    def click_sauces_section(self):
        """Кликает по секции 'Соусы'"""
        self.wait_for_element_visibility(MainPageLocators.SAUCES_SECTION)
        self.click_element(MainPageLocators.SAUCES_SECTION)
    
    @allure.step("Нажатие на секцию 'Начинки'")
    def click_fillings_section(self):
        """Кликает по секции 'Начинки'"""
        self.wait_for_element_visibility(MainPageLocators.FILLINGS_SECTION)
        self.click_element(MainPageLocators.FILLINGS_SECTION)
    
    @allure.step("Нажатие на булку")
    def click_bun_item(self):
        """Кликает по булке"""
        self.wait_for_element_visibility(MainPageLocators.BUN_ITEM)
        self.click_element(MainPageLocators.BUN_ITEM)
    
    @allure.step("Нажатие на кнопку 'Личный кабинет'")
    def click_profile_button(self):
        """Кликает по кнопке 'Личный кабинет'"""
        # Сначала закрываем модальное окно, если оно есть
        self.close_modal_if_present()
        
        # Дополнительная проверка, не находимся ли мы уже в профиле
        if self.is_on_profile_page():
            return  # Уже в профиле, ничего не делаем
        
        # Ожидаем, пока кнопка станет кликабельной
        self.wait_for_element_visibility(MainPageLocators.PROFILE_BUTTON)
        self.wait_for_element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)
        
        # Пытаемся кликнуть
        self.click_element(MainPageLocators.PROFILE_BUTTON)
    
    @allure.step("Нажатие на соус")
    def click_sauce_item(self):
        """Кликает по соусу"""
        self.wait_for_element_visibility(MainPageLocators.SAUCE_ITEM)
        self.click_element(MainPageLocators.SAUCE_ITEM)
    
    @allure.step("Нажатие на начинку")
    def click_filling_item(self):
        """Кликает по начинке"""
        self.wait_for_element_visibility(MainPageLocators.FILLING_ITEM)
        self.click_element(MainPageLocators.FILLING_ITEM)
    
    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def click_order_button(self):
        """Кликает по кнопке 'Оформить заказ'"""
        self.wait_for_element_visibility(MainPageLocators.ORDER_BUTTON)
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Нажатие кнопки 'Лента заказов'")
    def click_order_feed_button(self):
        """Кликает по кнопке 'Лента заказов'"""
        self.wait_for_element_visibility(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Закрытие модального окна")
    def close_modal(self):
        """Закрывает модальное окно"""
        self.wait_for_element_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Закрытие любых модальных окон")
    def close_any_modals(self):
        """Закрывает любые модальные окна, если они есть"""
        # Пытаемся закрыть основное модальное окно
        try:
            self.wait_for_element_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)
            return
        except:
            pass
            
        # Проверяем наличие модального окна с предупреждением
        try:
            self.wait_for_element_visibility(MainPageLocators.WARNING_MODAL)
            self.click_element(MainPageLocators.WARNING_MODAL_CLOSE_BUTTON)
            self.wait_for_element_invisibility(MainPageLocators.WARNING_MODAL)
        except:
            # Если модального окна нет, просто продолжаем
            pass
    
    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        """Проверяет видимость модального окна"""
        try:
            self.wait_for_element_visibility(MainPageLocators.MODAL_WINDOW, time=1)
            return True
        except:
            return False
        
    @allure.step("Проверка наличия модального окна")
    def is_modal_present(self, timeout=1):
        """Проверяет наличие модального окна"""
        try:
            self.wait_for_element_visibility(MainPageLocators.MODAL_OVERLAY, time=timeout)
            return True
        except:
            return False
    
    @allure.step("Проверка, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверяет, что модальное окно закрыто"""
        return not self.is_modal_visible()
    
    @allure.step("Получение значения счетчика булок")
    def get_bun_counter(self):
        """Получает значение счетчика булок"""
        self.wait_for_element_visibility(MainPageLocators.BUN_COUNTER)
        return self.get_text(MainPageLocators.BUN_COUNTER)
    
    @allure.step("Получение значения счетчика соусов")
    def get_sauce_counter(self):
        """Получает значение счетчика соусов"""
        self.wait_for_element_visibility(MainPageLocators.SAUCE_COUNTER)
        return self.get_text(MainPageLocators.SAUCE_COUNTER)
    
    @allure.step("Получение значения счетчика начинок")
    def get_filling_counter(self):
        """Получает значение счетчика начинок"""
        self.wait_for_element_visibility(MainPageLocators.FILLING_COUNTER)
        return self.get_text(MainPageLocators.FILLING_COUNTER)
    
    @allure.step("Получение номера заказа после оформления")
    def get_order_number(self):
        """Получает номер заказа после оформления"""
        try:
            self.wait_for_element_visibility(MainPageLocators.ORDER_CONFIRMATION_NUMBER)
            return self.get_text(MainPageLocators.ORDER_CONFIRMATION_NUMBER).strip('#')
        except:
            # Используем резервный локатор
            try:
                order_number_element = self.find_element(MainPageLocators.ORDER_NUMBER_FALLBACK)
                return order_number_element.text.strip('#')
            except:
                return None
    
    @allure.step("Проверка активности секции 'Булки'")
    def is_buns_section_active(self):
        """Проверяет, активна ли секция 'Булки'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.BUNS_SECTION_ACTIVE, time=1)
            return True
        except:
            return False
        
    @allure.step("Проверка активности секции 'Соусы'")
    def is_sauces_section_active(self):
        """Проверяет, активна ли секция 'Соусы'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.SAUCES_SECTION_ACTIVE, time=1)
            return True
        except:
            return False
    
    @allure.step("Проверка активности секции 'Начинки'")
    def is_fillings_section_active(self):
        """Проверяет, активна ли секция 'Начинки'"""
        try:
            self.wait_for_element_visibility(MainPageLocators.FILLINGS_SECTION_ACTIVE, time=1)
            return True
        except:
            return False
        
    @allure.step("Проверка, что мы на главной странице")
    def is_on_main_page(self):
        """Проверяет, что текущая страница - главная"""
        current_url = self.get_current_url()
        # Удаляем параметры и завершающий слеш для сравнения
        clean_url = current_url.split('?')[0].rstrip('/')
        clean_main_page_url = MAIN_PAGE_URL.rstrip('/')
        
        # Проверяем, что URL соответствует главной странице или содержит ее
        return clean_url == clean_main_page_url or clean_main_page_url in clean_url
    
    @allure.step("Проверка, что мы на странице конструктора")
    def is_on_constructor_page(self):
        """Проверяет, что текущая страница - конструктор"""
        return CONSTRUCTOR_URL in self.get_current_url()
    
    @allure.step("Проверка, что мы на странице ленты заказов")
    def is_on_order_feed_page(self):
        """Проверяет, что текущая страница - лента заказов"""
        return ORDER_FEED_URL in self.get_current_url()
    
    @allure.step("Проверка, что мы в истории заказов")
    def is_on_order_history_page(self):
        """Проверяет, что текущая страница - история заказов"""
        current_url = self.get_current_url()
        # Удаляем параметры для сравнения
        current_url = current_url.split('?')[0]
        return current_url.startswith(ORDER_HISTORY_URL)
    
    @allure.step("Проверка, что мы в профиле")
    def is_on_profile_page(self):
        """Проверяет, что текущая страница - профиль"""
        current_url = self.get_current_url()
        # Удаляем параметры для сравнения
        clean_url = current_url.split('?')[0]
        
        # Проверяем, что URL содержит путь профиля
        return PROFILE_URL in clean_url
    
    @allure.step("Закрытие модального окна, если оно присутствует")
    def close_modal_if_present(self):
        """Закрывает модальное окно, если оно присутствует"""
        if self.is_modal_visible():
            self.close_modal()
            self.wait_for_modal_to_close()

    @allure.step("Проверка, что мы на странице сброса пароля")
    def is_on_reset_password_page(self):
        """Проверяет, что текущая страница - страница сброса пароля"""
        current_url = self.get_current_url()
        # Удаляем параметры и завершающий слеш для сравнения
        clean_url = current_url.split('?')[0].rstrip('/')
        reset_password_url = RESET_PASSWORD_URL.rstrip('/')
        
        # Проверяем, что URL содержит путь к странице сброса пароля
        return reset_password_url in clean_url
        
    @allure.step("Проверка, что заголовок модального окна содержит текст")
    def is_modal_title_contains(self, text):
        """Проверяет, что заголовок модального окна содержит указанный текст"""
        return self.is_text_present_in_element(MainPageLocators.MODAL_TITLE, text)

    @allure.step("Получение числового значения счетчика булки")
    def get_bun_counter_value(self):
        """Возвращает числовое значение счетчика булки"""
        counter_text = self.get_bun_counter()
        try:
            return int(counter_text) if counter_text else 0
        except (ValueError, TypeError):
            return 0

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_modal_to_close(self):
        """Ожидает закрытия модального окна"""
        self.wait_for_element_invisibility(MainPageLocators.MODAL_WINDOW)