from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)

        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        input_password1.send_keys(password)

        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        input_password2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.url, "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
