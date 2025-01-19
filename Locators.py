from selenium.webdriver.common.by import By
class Locators:
    LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]') #кнопка войти в аккаунт
    EMAIL = (By.CSS_SELECTOR, 'input[name="name"]') #поле вводa Email
    NAME = (By.CSS_SELECTOR, 'input[name="name"]') #поле ввода имени
    PASSWORD = (By.NAME, 'Пароль') #поле ввода пароля
    AUTH_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]') # кнопка Войти
    PERS_ACCOUNT_BUTTON= (By.CSS_SELECTOR, 'a[href*="/account"]') # кнопка личный кабинет
    PLACE_AN_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') # кнопка оформить заказ
    AUTH_BUTTON_ON_PASSWORD_RECOVERY =(By.CSS_SELECTOR,'a[href*="/login"]') # кнопка войти на странице восстановления пароля
    AUTH_BUTTON_ON_REGISTRATION_FORM = (By.CSS_SELECTOR,'a[href*="/login"]') # кнопка войти на странице регистрации
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]') # кнопка выход
    SAUSE_BUTTON =(By.XPATH, '//span[contains(text(),"Соусы")]/parent::*') # кнопка соусы
    BREAD_BUTTON =(By.XPATH, '//span[contains(text(),"Булки")]/parent::*') # кнопка булки
    TOPPINGS_BUTTON =(By.XPATH, '//span[contains(text(),"Начинки")]/parent::*') # кнопка начинки
    SAVE_BUTTON = (By.XPATH,'//button[contains(text(),"Сохранить")]') # кнопка сохранить в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]') # кнопка конструктор
    LOGO =(By.TAG_NAME, 'svg') # кликабельное лого
    REGISTER_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]') # кнопка зарегестрироваться
    INPUT_ERROR = (By.CLASS_NAME,'input__error') #сообщение о некорректном пароле

