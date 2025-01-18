from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locators
from constants import Constants


class TestNavigationToPersonalAccount:

    # успешный переход по клику на кнопку "личный кабинет"
    def test_successful_redirect_to_personal_account_by_button(self, driver):

        driver.get(Constants.URL_LOGIN)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERS_ACCOUNT_BUTTON))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SAVE_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
