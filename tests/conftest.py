import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from utils.api_helper import create_user, delete_user
from urls import ORDER_FEED_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from pages.reset_password_page import ResetPasswordPage

@allure.step("Инициализация драйвера браузера")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для инициализации браузера с автоматическим управлением драйверами"""
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # Отключаем сохранение паролей
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), 
            options=options
        )
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        # Отключаем сохранение паролей
        options.set_preference("signon.rememberSignons", False)
        
        # Используем webdriver_manager для автоматического определения местоположения Firefox
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    
    yield driver
    driver.quit()

@allure.step("Инициализация главной страницы")
@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    main_page = MainPage(driver)
    main_page.open()
    yield main_page
    # Гарантированное закрытие модального окна после каждого теста
    main_page.close_modal_if_present()

@allure.step("Инициализация страницы входа")
@pytest.fixture
def login_page(driver, main_page):
    """Фикстура для страницы входа"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим на страницу входа
    main_page.click_login_button()
    
    login_page = LoginPage(driver)
    return login_page

@allure.step("Инициализация страницы восстановления пароля")
@pytest.fixture
def forgot_password_page(driver, main_page, login_page):
    """Фикстура для страницы восстановления пароля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим на страницу восстановления пароля
    login_page.click_forgot_password_link()
    
    # Проверяем, что мы на нужной странице
    if not main_page.is_on_forgot_password_page():
        print(f"Не на странице восстановления пароля. Текущий URL: {main_page.driver.current_url}")
        # Попробуем перейти напрямую
        main_page.driver.get(FORGOT_PASSWORD_URL)
    
    return ForgotPasswordPage(driver)

@allure.step("Инициализация страницы профиля")
@pytest.fixture
def profile_page(driver, registered_user, main_page):
    """Фикстура для страницы профиля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Логинимся
    login_page = LoginPage(driver)
    login_page.enter_email(registered_user["email"])
    login_page.enter_password(registered_user["password"])
    login_page.click_login_button()
    
    # Закрываем модальное окно после логина, если оно появилось
    main_page.close_modal_if_present()
    
    # Переходим в профиль
    main_page.click_profile_button()
    
    # Дополнительная проверка, что мы в профиле
    assert main_page.is_on_profile_page(), "Не перешли на страницу профиля"
    
    return ProfilePage(driver)

@allure.step("Создание тестового пользователя через API")
@pytest.fixture
def registered_user():
    """Фикстура для создания тестового пользователя через API"""
    user_data = create_user()
    yield user_data
    if user_data and "token" in user_data:
        delete_user(user_data["token"])

@allure.step("Инициализация страницы сброса пароля")
@pytest.fixture
def reset_password_page(driver, main_page, registered_user, forgot_password_page):
    """Фикстура для страницы сброса пароля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Вводим email и нажимаем "Восстановить"
    forgot_password_page.enter_email(registered_user["email"])
    forgot_password_page.click_restore_button()
    
    # Проверяем, что мы на нужной странице
    if not main_page.is_on_reset_password_page():
        print(f"Не на странице сброса пароля. Текущий URL: {main_page.driver.current_url}")
        # Попробуем перейти напрямую
        driver.get(RESET_PASSWORD_URL)
    
    # ПРАВИЛЬНО: используем локатор из ResetPasswordPageLocators
    reset_page = ResetPasswordPage(driver)
    reset_page.wait_for_password_field_to_be_visible()
    
    return reset_page

@allure.step("Инициализация страницы ленты заказов")
@pytest.fixture
def order_feed_page(driver, main_page):
    """Фикстура для страницы ленты заказов"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим на страницу ленты заказов
    main_page.click_order_feed_button()
    
    # Проверяем, что мы на нужной странице
    if not main_page.is_on_order_feed_page():
        print(f"Не на странице ленты заказов. Текущий URL: {main_page.driver.current_url}")
        # Попробуем перейти напрямую
        driver.get(ORDER_FEED_URL)
    
    order_feed_page = OrderFeedPage(driver)
    
    # Сохраняем начальные значения счетчиков
    try:
        order_feed_page.initial_total_orders = order_feed_page.get_total_orders()
        order_feed_page.initial_today_orders = order_feed_page.get_today_orders()
    except:
        # Если не удалось получить счетчики, устанавливаем значения по умолчанию
        order_feed_page.initial_total_orders = 0
        order_feed_page.initial_today_orders = 0
    
    return order_feed_page

@allure.step("Оформление тестового заказа")
@pytest.fixture
def placed_order(driver, registered_user, main_page, login_page):
    """Фикстура для оформления тестового заказа"""
    # Логинимся
    main_page.click_login_button()
    login_page.enter_email(registered_user["email"])
    login_page.enter_password(registered_user["password"])
    login_page.click_login_button()
    
    # Добавляем ингредиенты
    main_page.click_bun_item()
    main_page.close_modal()
    main_page.wait_for_modal_to_close()
    main_page.click_sauce_item()
    main_page.close_modal()
    main_page.wait_for_modal_to_close()
    
    # Оформляем заказ
    main_page.click_order_button()
    
    # Ждем появления номера заказа
    order_number = main_page.get_order_number()
    
    yield {"number": order_number}