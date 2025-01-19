from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from Locators import Locators

class TestNavigationToConstructor:
#успешный переход во вкладку конструктор из личного кабинета по кнопке конструктор
    def test_successful_redirect_to_constructor_from_personal_account(self, driver):
        driver.get(Constants.URL_LOGIN)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERS_ACCOUNT_BUTTON))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SAVE_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == Constants.URL

# успешный переход во вкладку конструктор из личного кабинета по клику на лиготип
    def test_successful_redirect_to_constructor_from_personal_account_by_click_on_logo(self,driver):
        driver.get(Constants.URL_LOGIN)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERS_ACCOUNT_BUTTON))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SAVE_BUTTON))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == Constants.URL


