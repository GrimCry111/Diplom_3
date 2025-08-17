# Убедитесь, что нет пробелов в конце BASE_URL
BASE_URL = "https://stellarburgers.nomoreparties.site"

# URL для веб-интерфейса
MAIN_PAGE_URL = BASE_URL
CONSTRUCTOR_URL = f"{BASE_URL}/constructor"
ORDER_FEED_URL = f"{BASE_URL}/feed"
PROFILE_URL = f"{BASE_URL}/account"
ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"
LOGIN_URL = f"{BASE_URL}/login"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"

# URL для API
API_BASE_URL = f"{BASE_URL}/api"
REGISTER_API_URL = f"{API_BASE_URL}/auth/register"
LOGIN_API_URL = f"{API_BASE_URL}/auth/login"
USER_API_URL = f"{API_BASE_URL}/auth/user"
INGREDIENTS_API_URL = f"{API_BASE_URL}/ingredients"
ORDERS_API_URL = f"{API_BASE_URL}/orders"