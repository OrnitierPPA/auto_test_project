from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), "There are item(s) in the basket"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket not empty"