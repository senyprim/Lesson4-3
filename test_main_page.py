import  pytest
from pages.main_page import MainPage
from pages.cart_page import CartPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser, link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser, link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"):

        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser, link="http://selenium1py.pythonanywhere.com"):
    page = CartPage(browser, link)
    page.open()
    page.go_to_card_page()
    page.should_not_be_disappeared_product()
    page.should_be_success_message()

