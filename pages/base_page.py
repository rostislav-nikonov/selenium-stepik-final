import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is missing"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not logged in"

    def solve_quiz_and_get_code(self):
        alert = WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
        value = float(alert.text.split()[2])
        alert.send_keys(str(math.log(abs(12 * math.sin(value)))))
        alert.accept()
        try:
            code_alert = WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        except TimeoutException:
            return
        print(f"Your code: {code_alert.text}")
        code_alert.accept()
