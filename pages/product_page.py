from .base_page import BasePage
from .locators import ProductPageLocators

from selenium import webdriver


class ProductPage(BasePage):
    def add_product_in_busket(self):
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.alert_present(10)
        self.solve_quiz_and_get_code()
        assert product_name == self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text, "The product was not added to the basket"
        print("Товар добавлен в корзину: ", product_name)
        assert product_cost == self.browser.find_element(*ProductPageLocators.BUSKET_COST).text, "The price does not match"
        print("Цена товара совпадает с ценой корзины: ", product_cost)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message discovered"
    
    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message discovered"