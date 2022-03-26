from .base_page import BasePage
from .locators import ProductPageLocators
from math import log, sin
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def action_on_product_page(self):
        self.click_on_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_basket_message_title()
        self.check_basket_message_price()

    def click_on_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_basket_message_title(self):
        title_in_basket_message = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_IN_BASKET_MESSAGE).text
        product_title = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT).text
        assert title_in_basket_message == product_title, 'Title in massage and product title not match'

    def check_basket_message_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, 'Price in massage and product price not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), "Success message is presented, but should not be"

    def should_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), "Success message is not disappeared, but should be"



