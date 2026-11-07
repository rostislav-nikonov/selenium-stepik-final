from uuid import uuid4

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


PRODUCT_URL = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LOGIN_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.need_review
@pytest.mark.parametrize("offer", [
    0, 1, 2, 3, 4, 5, 6,
    pytest.param(7, marks=pytest.mark.xfail(
        reason="Known product-name bug in offer7", raises=AssertionError, strict=True
    )),
    8, 9,
])
def test_guest_can_add_product_to_basket(browser, offer):
    page = ProductPage(browser, f"{PRODUCT_URL}?promo=offer{offer}")
    page.open()
    name = page.get_product_name()
    price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket(name)
    page.should_be_basket_total(price)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty()
    basket.should_have_empty_basket_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="Adding a product shows a success message", raises=AssertionError, strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message remains on the page", raises=AssertionError, strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_URL)
        login_page.open()
        login_page.register_new_user(f"qa-{uuid4().hex}@example.org", f"Test-{uuid4().hex}")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        name = page.get_product_name()
        price = page.get_product_price()
        page.add_product_to_basket()
        page.should_be_product_in_basket(name)
        page.should_be_basket_total(price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()
