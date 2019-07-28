import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


@pytest.mark.login
class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print("запуск фикстуры setup")
        self.browser = browser
        page = LoginPage(self.browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org","password_login")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_in_basket()
        page.should_be_product_cost_in_basket()

    def test_user_cant_see_success_message(self, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_basket()
    page.should_be_product_cost_in_basket()


def test_guest_cant_see_success_message(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser, link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" ):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser, link="http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"):
    page = CartPage(browser, link)
    page.open()
    page.go_to_card_page()
    page.should_not_be_disappeared_product()
    page.should_be_success_message()