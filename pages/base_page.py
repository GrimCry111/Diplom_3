from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"
        self.wait = WebDriverWait(driver, 15)  
    
    def find_element(self, locator, time=15):
        """Находит элемент на странице с увеличенным таймаутом"""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )
    
    def find_elements(self, locator, time=15):
        """Находит все элементы по локатору с увеличенным таймаутом"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}"
        )
    
    def click_element(self, locator, time=15):
        """Кликает по элементу с ожиданием кликабельности"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
        element.click()
        return element
    
    def send_keys(self, locator, text, time=15):
        """Вводит текст в поле с ожиданием видимости и кликабельности"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Поле ввода {locator} не кликабельно"
        )
        element.clear()
        element.send_keys(text)
        return element
    
    def get_text(self, locator, time=15):
        """Получает текст элемента с ожиданием видимости"""
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
        return element.text
    
    def get_current_url(self):
        """Возвращает текущий URL с ожиданием изменения"""
        return self.wait.until(
            lambda driver: driver.current_url,
            message="Не удалось получить текущий URL"
        )
    
    def wait_for_url_change(self, expected_url, time=15):
        """Ожидает изменения URL"""
        return self.wait.until(
            EC.url_to_be(expected_url),
            message=f"URL не изменился на ожидаемый {expected_url}"
        )
    
    def wait_for_element_visibility(self, locator, time=15):
        """Ожидает видимости элемента"""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
    
    def wait_for_element_invisibility(self, locator, time=15):
        """Ожидает скрытия элемента"""
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент {locator} все еще виден"
        )
    
    def wait_for_element_attribute(self, locator, attribute, value, time=15):
        """Ожидает появления определенного атрибута у элемента"""
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value),
            message=f"Атрибут {attribute} не содержит {value} у элемента {locator}"
        )
    
    def wait_for_element_text(self, locator, text, time=15):
        """Ожидает появления определенного текста в элементе"""
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Текст '{text}' не найден в элементе {locator}"
        )
    
    def open(self):
        """Открывает главную страницу"""
        self.driver.get(self.base_url)
        # Дополнительное ожидание загрузки страницы
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Соберите бургер')]")),
            message="Главная страница не загрузилась"
        )

    def close_warning_popup(self):
        """Закрывает всплывающее окно предупреждения"""
        try:
            # Проверяем, есть ли окно
            self.wait_for_element_visibility((By.XPATH, "//div[contains(@class, 'popup')]"), time=5)
            # Кликаем по кнопке "ОК"
            self.click_element(MainPageLocators.OK_BUTTON)
        except TimeoutException:
            # Если окно не появилось, ничего не делаем
            pass