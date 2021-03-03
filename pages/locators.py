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

    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    MESSAGE_CART_PRICE = (By.XPATH, "//div[@id='messages']/div[contains(@class, 'alert-info')]//strong")
