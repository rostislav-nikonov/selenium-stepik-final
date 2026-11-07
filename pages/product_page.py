from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_be_product_in_basket(self, name):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Product confirmation is missing"
        actual_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert actual_name == name, f"Expected product {name!r}, got {actual_name!r}"

    def should_be_basket_total(self, price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total is missing"
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert total == price, f"Expected basket total {price!r}, got {total!r}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Unexpected success message"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"
