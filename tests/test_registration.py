from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import email_helper
from Locators import Locators
from constants import Constants


class TestRegistration:
    # успешная регистрация
    def test_successful_registration(self, driver):
        driver.get(Constants.URL_REGISTER)
        name = driver.find_elements(*Locators.NAME)[0]
        name.send_keys('Barosha')
        email_field = driver.find_elements(*Locators.EMAIL)[1]
        new_email = email_helper.email_generator()
        email_field.send_keys(new_email)
        driver.find_element(*Locators.PASSWORD).send_keys('108035')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON))
        email_field = driver.find_elements(*Locators.EMAIL)[0]
        email_field.send_keys(new_email)
        driver.find_element(*Locators.PASSWORD).send_keys('108035')
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == Constants.URL

    # ошибка при некорректном пароля(5 символов)
    def test_getting_allert_when_password_contains_five_symbols(self, driver):
        driver.get(Constants.URL_REGISTER)
        name = driver.find_elements(*Locators.NAME)[0]
        name.send_keys('Barosha')
        email = driver.find_elements(*Locators.EMAIL)[1]
        email.send_keys(email_helper.email_generator())
        driver.find_element(*Locators.PASSWORD).send_keys('10803')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.INPUT_ERROR).is_displayed()
