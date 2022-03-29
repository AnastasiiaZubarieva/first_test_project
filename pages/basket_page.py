from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def sould_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Products is presented in basket, but should not be"

    def sould_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket not empty, but should be"