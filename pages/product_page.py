from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_added_product_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_TO_BASKET).text

    def get_price_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_TO_BASKET).text

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button add to basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_TO_BASKET), "Success message is presented, but should not be"

    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME_TO_BASKET), "Success message is presented, but should not be"












