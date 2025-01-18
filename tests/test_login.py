from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locators
from constants import Constants


class TestLogin:

    # успешный вход по кнопке "войти в аккаунт" на главной странице
    def test_successful_login_by_login_button(self,driver):
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# успешный вход через кнопку "личный кабинет"
    def test_succsessful_login_by_personal_account_button(self,driver):
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# успешный вход через кнопку в форме регистрации
    def test_successful_login_in_registration_form(self,driver):
        driver.get(Constants.URL_REGISTER)
        driver.find_element(*Locators.AUTH_BUTTON_ON_REGISTRATION_FORM).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# успешный вход через кнопку в форме восстановления пароля
    def test_successful_login_in_password_recovery_form(self,driver):
        driver.get(Constants.URL_PASSWORD_RECOVERY)
        driver.find_element(*Locators.AUTH_BUTTON_ON_PASSWORD_RECOVERY).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PLACE_AN_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
