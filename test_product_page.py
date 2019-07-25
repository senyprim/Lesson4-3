import pytest
from pages.product_page import ProductPage
import time



def test_guest_can_add_product_to_cart(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.get_product_name() == page.get_added_product_to_basket(), f"Товар со страницы {link} не соответствует товару в корзине после добавления"
    assert page.get_product_price() == page.get_price_to_basket(),f"Цена со страницы {link} не соответствует цене товара который добавили"


def test_guest_cant_see_success_message(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()