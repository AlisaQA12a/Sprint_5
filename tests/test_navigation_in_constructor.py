
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locators

class TestNavigationInConstructor:
#успешный переход в раздел соусы из раздела булки
    def test_successful_redirect_from_bred_to_sause(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON))
        sause = driver.find_element(*Locators.SAUSE_BUTTON)
        sause_class = sause.get_attribute('class')
        sause.click()
        sause_new_class = sause.get_attribute('class')
        assert sause_class != sause_new_class

#успешный переход в раздел булки из раздела соусы
    def test_successful_redirect_from_sause_to_bread(self,driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERS_ACCOUNT_BUTTON))
        sause = driver.find_element(*Locators.SAUSE_BUTTON)
        sause.click()
        bread = driver.find_element(*Locators.BREAD_BUTTON)
        bread_class = bread.get_attribute('class')
        bread.click()
        bread_new_class = bread.get_attribute('class')
        assert bread_class != bread_new_class

#успешный переход в раздел начинки из раздела булки
    def test_successful_redirect_from_bread_to_toppings(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PERS_ACCOUNT_BUTTON))
        topping = driver.find_element(*Locators.TOPPINGS_BUTTON)
        topping_class = topping.get_attribute('class')
        topping.click()
        topping_new_class = topping.get_attribute('class')
        assert topping_class != topping_new_class



