from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    TITLE_PRODUCT_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    TITLE_PRODUCT = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    SUCCES_MESSAGE = (By.CSS_SELECTOR,'.alert-success')

