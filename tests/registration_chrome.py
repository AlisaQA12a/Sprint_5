import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def email_generator(length = 7):
    prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return prefix + '@mail.ru'

#успешная регистрация

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/register')
name = driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[0]
name.send_keys('Barosha')
email= driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[1]
email.send_keys(email_generator())
driver.find_element(By.NAME, 'Пароль').send_keys('108035')
driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Войти")]')))
driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
driver.quit()


#ошибка при некорректном пароля(5 символов)

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/register')
name = driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[0]
name.send_keys('Barosha')
email= driver.find_elements(By.CSS_SELECTOR, 'input[name="name"]')[1]
email.send_keys(email_generator())
driver.find_element(By.NAME, 'Пароль').send_keys('10803')
driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
driver.find_element(By.CLASS_NAME, 'input__error')
driver.quit()
