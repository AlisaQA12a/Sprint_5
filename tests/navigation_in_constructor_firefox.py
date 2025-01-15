from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#успешный переход в раздел соусы из раздела булки

driver = webdriver.Firefox()
driver.get('https://stellarburgers.nomoreparties.site')
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p')))
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]').is_displayed()
driver.quit()

#успешный переход в раздел булки из раздела соусы

driver = webdriver.Firefox()
driver.get('https://stellarburgers.nomoreparties.site')
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p')))
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p').is_displayed()
driver.quit()

#успешный переход в раздел начинки из раздела булки

driver = webdriver.Firefox()
driver.get('https://stellarburgers.nomoreparties.site')
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[4]/p')))
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[4]/p').is_displayed()
driver.quit()