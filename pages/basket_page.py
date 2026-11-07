from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Basket contains products"

    def should_have_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty basket message is missing"
        message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert message.strip(), "Empty basket message has no text"
