from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#успешный выход из аккаунта по кнопке "Выйти" в личном кабинете

driver = webdriver.Firefox()
driver.get('https://stellarburgers.nomoreparties.site/login')
email= driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[0]
email.send_keys('babl2234@ya.ru')
driver.find_element(By.NAME, 'Пароль').send_keys('123457')
driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='/account']")))
driver.find_element(By.CSS_SELECTOR, "a[href*='/account']").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Выход")]')))
driver.find_element(By.XPATH, '//button[contains(text(),"Выход")]').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Войти")]')))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
driver.quit()