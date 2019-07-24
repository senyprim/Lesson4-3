from .base_page import BasePage
from .locators import MainPageLocators
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.shoul_be_aqual_price_after_added()
        self.should_be_equal_product_name_after_added()

    def get_product_name(self):
        return self.browser.find_element(*MainPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text

    def get_added_product_to_basket(self):
        return self.browser.find_element(*MainPageLocators.ADDED_PRODUCT_NAME_TO_BASKET).text

    def get_price_to_basket(self):
        return self.browser.find_element(*MainPageLocators.PRICE_TO_BASKET).text

    def should_be_equal_product_name_after_added(self):
        assert self.get_product_name()==self.get_added_product_to_basket(),"Товар в корзине должен соответствовать товару который добавили"

    def shoul_be_aqual_price_after_added(self):
        assert  self.get_product_price()==self.get_price_to_basket(),"Цена корзины должна соответствовать, цене товара который добавили"

    def should_be_catalogue(self):
        assert "catalogue" in self.browser.current_url(),"Неверный url страницы продукта"

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*MainPageLocators.ADD_TO_BASKET_BUTTON), "Button add to basket is not presented"










