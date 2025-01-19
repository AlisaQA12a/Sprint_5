from constants import Constants
from Locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
#успешный выход из аккаунта по кнопке "Выйти" в личном кабинете
    def test_successful_logout_by_logout_button_in_personal_account(self,driver):
        driver.get(Constants.URL_LOGIN)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON))
        assert driver.current_url == Constants.URL_LOGIN


