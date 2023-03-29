from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert browser.current_url, "is not found"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REG_FORM), "Is not presented"
        assert True