from .pages.main_page import MainPage
from .pages.login_page import LoginPage

from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

def test_on_the_existence_of_login_and_registration_forms(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()