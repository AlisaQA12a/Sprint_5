import pytest
from selenium import webdriver

from constants import Constants
from Locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()
