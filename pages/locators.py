from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]//p[@class='price_color']")

    MSG_PRODUCT_ADDED_TO_CART = (By.XPATH, "//div[@id='messages']/div[1]")
    MSG_PRODUCT_ADDED_TO_CART_PRICE = (By.XPATH, "//div[@id='messages']/div[last()]")
    MSG_PRODUCT_TITLE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    MSG_PRODUCT_PRICE = (By.XPATH, "//div[@id='messages']/div[last()]//strong")
