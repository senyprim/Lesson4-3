from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_PRODUCT_NAME_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1) strong")
    PRICE_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-of-type(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_PAGE_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class CartPageLocators:
    PRODUCT_IN_BASKET=(By.CSS_SELECTOR,".basket-items .row h3 a")
    MESAGE_EMPTY_BASKET=(By.CSS_SELECTOR,".content #content_inner p")


