import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import FORGOT_PASSWORD_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"
        self.wait = WebDriverWait(driver, 15)  # Увеличенный таймаут до 15 секунд
    
    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator, time=15):
        """Находит элемент на странице с увеличенным таймаутом"""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )
    
    @allure.step("Поиск всех элементов по локатору")
    def find_elements(self, locator, time=15):
        """Находит все элементы по локатору с увеличенным таймаутом"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}"
        )
    
    @allure.step("Клик по элементу")
    def click_element(self, locator, time=15):
        """Кликает по элементу с ожиданием кликабельности"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
        element.click()
        return element
    
    @allure.step("Ввод текста в поле")
    def send_keys(self, locator, text):
        """Вводит текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    @allure.step("Получение текста элемента")
    def get_text(self, locator, time=15):
        """Получает текст элемента с ожиданием видимости"""
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
        return element.text
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Возвращает текущий URL с ожиданием изменения"""
        return self.wait.until(
            lambda driver: driver.current_url,
            message="Не удалось получить текущий URL"
        )
    
    def scroll_to_element(self, locator, time=10):
        """Прокручивает к элементу"""
        element = self.find_element(locator, time)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element
    
    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visibility(self, locator, time=15):
        """Ожидает видимости элемента"""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
    
    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_invisibility(self, locator, time=15):
        """Ожидает скрытия элемента"""
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент {locator} все еще виден"
        )
    
    @allure.step("Ожидание появления атрибута у элемента")
    def wait_for_element_attribute(self, locator, attribute, value, time=15):
        """Ожидает появления определенного атрибута у элемента"""
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value),
            message=f"Атрибут {attribute} не содержит {value} у элемента {locator}"
        )
    
    @allure.step("Ожидание появления текста в элементе")
    def wait_for_element_text(self, locator, text, time=15):
        """Ожидает появления определенного текста в элементе"""
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Текст '{text}' не найден в элементе {locator}"
        )
    
    @allure.step("Ожидание доступа к элементу")
    def wait_for_element_to_be_clickable(self, locator, time=10):
        """Ожидает, пока элемент станет кликабельным"""
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен за {time} секунд"
        )
    
    @allure.step("Открытие главной страницы")
    def open(self):
        """Открывает главную страницу"""
        self.driver.get(self.base_url)
        # Дополнительное ожидание загрузки страницы
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Соберите бургер')]")),
            message="Главная страница не загрузилась"
        )

    def is_element_visible(self, locator, time=5):
        """Проверяет видимость элемента"""
        try:
            self.wait_for_element_visibility(locator, time=time)
            return True
        except:
            return False

    def wait_for_url_contains(self, url_part, timeout=10):
        """Ожидает, пока URL не будет содержать определенную часть"""
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: url_part in driver.current_url,
            message=f"URL не содержит '{url_part}' за {timeout} секунд"
        )

    def is_on_forgot_password_page(self):
        """Проверяет, что мы на странице восстановления пароля"""
        current_url = self.driver.current_url
        return FORGOT_PASSWORD_URL in current_url
    
    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url