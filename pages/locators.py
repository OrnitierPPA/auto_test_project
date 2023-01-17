from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASS = [By.XPATH, "//input[@id='id_login-password']"]
    REG_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REG_PASS = (By.XPATH, "//input[@id='id_registration-password1']")
    REG_PASS_CONF = (By.XPATH, "//input[@id='id_registration-password2']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:first-child')
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, 'div.alert:first-child > div.alertinner > strong')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    BUSKET_COST = (By.CSS_SELECTOR, 'div.alert > div.alertinner > p > strong')
    