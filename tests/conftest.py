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
    main_page.open()
    return main_page

@pytest.fixture
def login_page(driver):
    """Фикстура для страницы входа"""
    login_page = LoginPage(driver)
    login_page.open()
    return login_page

@pytest.fixture
def forgot_password_page(driver):
    """Фикстура для страницы восстановления пароля"""
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open()
    # Переходим на страницу восстановления пароля
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.click_forgot_password_link()
    return forgot_password_page

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
    
    # Переходим в профиль
    main_page.click_profile_button()
    
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