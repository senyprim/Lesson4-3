from .locators import CartPageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def should_not_be_disappeared_product(self):
        assert self.is_disappeared(*CartPageLocators.PRODUCT_IN_BASKET), "Корзина долна быть пуста"

    def should_not_be_success_product(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_BASKET), "В корзине есть товар а недолжно"

    def should_be_success_message(self):
        assert self.is_element_present(*CartPageLocators.MESAGE_EMPTY_BASKET), "В корзине нет сообщения пустой корзины"




