from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASS = [By.XPATH, "//input[@id='id_login-password']"]
    REG_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REG_PASS = (By.XPATH, "//input[@id='id_registration-password1']")
    REG_PASS_CONF = (By.XPATH, "//input[@id='id_registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "div.register_form > form.well > button.btn.btn-lg.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:first-child')
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, 'div.alert:first-child > div.alertinner > strong')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    BUSKET_COST = (By.CSS_SELECTOR, 'div.alert > div.alertinner > p > strong')


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "div.content > div > p > a")
    PRODUCTS = (By.CSS_SELECTOR, "form.basket_summary")