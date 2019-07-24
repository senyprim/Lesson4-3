from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK=(By.CSS_SELECTOR,"#registration_link_err")
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form_err")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_err")