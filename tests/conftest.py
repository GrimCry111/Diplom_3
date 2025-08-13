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
from urls import MAIN_PAGE_URL, LOGIN_URL, PROFILE_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from pages.reset_password_page import ResetPasswordPage

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
        
        # Правильно указываем путь к исполняемому файлу Firefox
        # ВАРИАНТ 1: Для стандартной установки
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        
        # ВАРИАНТ 2: Если стандартный путь не работает, попробуйте этот:
        # options.binary_location = r'C:\Users\Sokol\AppData\Local\Mozilla Firefox\firefox.exe'
        
        # Устанавливаем GeckoDriver через webdriver_manager
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    main_page = MainPage(driver)
    main_page.driver.get(MAIN_PAGE_URL)
    return main_page

@pytest.fixture
def login_page(driver):
    """Фикстура для страницы входа"""
    login_page = LoginPage(driver)
    login_page.driver.get(LOGIN_URL)
    return login_page

@pytest.fixture
def forgot_password_page(driver, main_page, login_page):
    """Фикстура для страницы восстановления пароля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим на страницу входа
    main_page.click_login_button()
    
    # Нажимаем на ссылку "Восстановить пароль"
    try:
        login_page.click_forgot_password_link()
    except Exception as e:
        print(f"Ошибка при переходе на страницу восстановления пароля: {str(e)}")
        # Если переход не удался, пробуем перезагрузить страницу и повторить
        main_page.driver.refresh()
        main_page.click_login_button()
        login_page.click_forgot_password_link()
    
    # Проверяем, что мы на нужной странице
    if not main_page.is_on_forgot_password_page():
        print(f"Не на странице восстановления пароля. Текущий URL: {main_page.driver.current_url}")
        # Попробуем перейти напрямую
        main_page.driver.get(FORGOT_PASSWORD_URL)    
    return ForgotPasswordPage(driver)

@pytest.fixture
def profile_page(driver, registered_user):
    """Фикстура для страницы профиля"""
    # Логинимся
    main_page = MainPage(driver)
    main_page.open()
    
    # Проверяем, не залогинен ли уже пользователь
    try:
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.enter_email(registered_user["email"])
        login_page.enter_password(registered_user["password"])
        login_page.click_login_button()
    except:
        # Если кнопка "Войти" не найдена, возможно, пользователь уже залогинен
        pass
    
    # ВАЖНО: Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим в профиль
    main_page.click_profile_button()
    
    # Дополнительная проверка, что мы в профиле
    main_page.wait_for_page_load(PROFILE_URL, timeout=25)
    
    return ProfilePage(driver)

@pytest.fixture
def order_feed_page(driver):
    """Фикстура для ленты заказов"""
    order_feed_page = OrderFeedPage(driver)
    order_feed_page.open()
    # Переходим на страницу ленты заказов
    main_page = MainPage(driver)
    main_page.click_order_feed_button()
    return order_feed_page

@pytest.fixture
def registered_user():
    """Фикстура для создания тестового пользователя через API"""
    user_data = create_user()
    yield user_data
    if user_data and "token" in user_data:
        delete_user(user_data["token"])

@pytest.fixture
def forgot_password_page(driver, main_page, login_page):
    """Фикстура для страницы восстановления пароля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Переходим на страницу входа
    main_page.click_login_button()
    
    # Нажимаем на ссылку "Восстановить пароль"
    login_page.click_forgot_password_link()
    
    return ForgotPasswordPage(driver)

@pytest.fixture
def reset_password_page(driver, main_page, forgot_password_page, registered_user):
    """Фикстура для страницы сброса пароля"""
    # Закрываем модальное окно, если оно есть
    main_page.close_modal_if_present()
    
    # Проверяем, не находимся ли мы уже на странице восстановления пароля
    current_url = main_page.driver.current_url
    if FORGOT_PASSWORD_URL not in current_url:
        # Если нет, переходим на страницу входа
        main_page.open()
        main_page.close_modal_if_present()
        
        # Переходим на страницу восстановления пароля
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
    
    # Вводим email и нажимаем "Восстановить"
    forgot_password_page.enter_email(registered_user["email"])
    forgot_password_page.click_restore_button()
    
    # Проверяем, что мы на нужной странице
    if not main_page.is_on_reset_password_page():
        print(f"Не на странице сброса пароля. Текущий URL: {main_page.driver.current_url}")
        # Попробуем перейти напрямую
        driver.get(RESET_PASSWORD_URL)
    
    return ResetPasswordPage(driver)