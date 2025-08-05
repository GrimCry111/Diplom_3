from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    """Локаторы для ленты заказов"""
    
    # Счетчики
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    
    # Заказы
    ORDER_ITEMS = (By.XPATH, "//li[contains(@class, 'OrderHistory_item')]")
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_item')][1]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'OrderHistory_text')]")  # Исправлено
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_MODAL_TITLE = (By.XPATH, "//h2[contains(text(), '#')]")
    ORDER_MODAL_INGREDIENTS = (By.XPATH, "//ul[contains(@class, 'OrderIngredients_list')]")
    
    # Заказы в работе
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orders')]/li")