from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASS = [By.XPATH, "//input[@id='id_login-password']"]
    REG_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REG_PASS = (By.XPATH, "//input[@id='id_registration-password1']")
    REG_PASS_CONF = (By.XPATH, "//input[@id='id_registration-password2']")
