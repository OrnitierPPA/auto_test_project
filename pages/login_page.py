from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "It's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field doesn't exist"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password field doesn't exist"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email field doesn't exist"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Registration password field doesn't exist"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_CONF), "Registration password confirm field doesn't exist"
        assert True