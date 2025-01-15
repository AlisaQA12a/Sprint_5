from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#успешный переход по клику на кнопку "личный кабинет"

driver = webdriver.Firefox()
driver.get('https://stellarburgers.nomoreparties.site/register')
driver.find_element(By.CSS_SELECTOR,'a[href*="/login"]').click()
email= driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[0]
email.send_keys('babl2234@ya.ru')
driver.find_element(By.NAME, 'Пароль').send_keys('123457')
driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Сохранить")]')))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
driver.quit()