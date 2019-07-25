from selenium.webdriver.common.by import By


class MainPageLocators(object):
    pass


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_PRODUCT_NAME_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1) strong")
    PRICE_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-of-type(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")