from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_displayed_added_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.MSG_PRODUCT_ADDED_TO_CART)

    def message_should_display_correct_product_title(self, product_title: str):
        assert product_title == self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def should_displayed_added_to_cart_product_price_message(self):
        assert self.is_element_present(*ProductPageLocators.MSG_PRODUCT_ADDED_TO_CART_PRICE)

    def message_should_display_correct_product_price(self, product_price: str):
        assert product_price == self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_PRICE).text

    def get_product_title(self) -> str:
        return self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_TITLE).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

