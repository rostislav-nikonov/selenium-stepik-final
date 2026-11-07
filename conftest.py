import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", default="en", help="Browser language, for example en or ru")
    parser.addoption("--headless", action="store_true", help="Run Chrome without visible windows")


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("CHROME_BINARY", "")
    language = request.config.getoption("language")
    options.add_argument(f"--lang={language}")
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    if request.config.getoption("headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
    service = Service(executable_path=os.environ.get("CHROMEDRIVER"))
    driver = webdriver.Chrome(service=service, options=options)
    try:
        yield driver
    finally:
        driver.quit()
