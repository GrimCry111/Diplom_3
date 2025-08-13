from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""

    # Соус, Начинка, Идентификатор, Резервный
    SAUCE_COUNTER = (By.XPATH, "//h3[contains(., 'Соус')]/ancestor::a//p[contains(@class, 'counter')]")
    FILLING_COUNTER = (By.XPATH, "//h3[contains(., 'Начинка')]/ancestor::a//p[contains(@class, 'counter')]")
    ORDER_CONFIRMATION_NUMBER = (By.XPATH, "//h2[contains(., 'идентификатор')]/following-sibling::p")
    ORDER_NUMBER_FALLBACK = (By.XPATH, "//p[contains(@class, 'text')]")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and contains(., 'Войти')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/constructor') or contains(@class, 'AppHeader_link_active')]")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and contains(., 'Оформить')]")
    
    # Секции ингредиентов
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(., 'Булки')]]")
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(., 'Соусы')]]")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(., 'Начинки')]]")
    
    # Активные секции
    BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[contains(., 'Булки')]]")
    SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[contains(., 'Соусы')]]")
    FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[contains(., 'Начинки')]]")
    
    # Ингредиенты - используем более гибкие локаторы
    BUN_ITEM = (By.XPATH, "//h3[contains(., 'Краторная')]/ancestor::a")
    SAUCE_ITEM = (By.XPATH, "//h3[contains(., 'Соус')]/ancestor::a")
    FILLING_ITEM = (By.XPATH, "//h3[contains(., 'Говяжий')]/ancestor::a")
    
    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal') and contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_TITLE = (By.XPATH, "//h2[contains(., 'Детали')]")
    
    # Счетчики ингредиентов
    BUN_COUNTER = (By.XPATH, "//h3[contains(., 'Краторная')]/ancestor::a//p[contains(@class, 'counter')]")
    SAUCE_COUNTER = (By.XPATH, "//h3[contains(., 'Соус')]/ancestor::a//p[contains(@class, 'counter')]")
    FILLING_COUNTER = (By.XPATH, "//h3[contains(., 'Говяжий')]/ancestor::a//p[contains(@class, 'counter')]")
    
    # Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
    
    # Подтверждение заказа
    ORDER_CONFIRMATION_TITLE = (By.XPATH, "//h2[contains(., 'идентификатор')]")
    ORDER_CONFIRMATION_NUMBER = (By.XPATH, "//p[contains(@class, 'Modal_order__number')]")
    ORDER_CONFIRMATION_TEXT = (By.XPATH, "//p[contains(., 'Ваш заказ начали готовить')]")
    
     # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    # Профиль
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    
    # Добавляем локатор для модального окна с предупреждением
    WARNING_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    WARNING_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    # Локатор для кнопки "ОК" в всплывающем окне
    OK_BUTTON = (By.XPATH, "//button[contains(., 'ОК')]")
