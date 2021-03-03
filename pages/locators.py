from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, "//*[@id='content_inner']/p/a")
    PRODUCT_LIST_FORM = (By.XPATH, "//form[@id='basket_formset']")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")

    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]//p[@class='price_color']")

    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    MESSAGE_CART_PRICE = (By.XPATH, "//div[@id='messages']/div[contains(@class, 'alert-info')]//strong")
