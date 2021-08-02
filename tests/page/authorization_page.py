from selenium.webdriver.common.by import By
from tests.page.page_manager import PagesManager


class AthorizationPageLocators:
    LOGIN_FIELD = (By.ID, 'com.ajaxsystems:id/login')
    PASSWORD_FIELD = (By.ID, 'com.ajaxsystems:id/password')
    AUTHORIZATION_BUTTON = (By.ID, 'com.ajaxsystems:id/next')
    ERROR_MESSAGE = (By.ID, 'com.ajaxsystems:id/snackbar_text')


class AuthorizationPage(object):

    def __init__(self, driver):
        self.pm = PagesManager(driver)

    def fill_fields(self, email, password):
        self.pm.locate_element(AthorizationPageLocators.LOGIN_FIELD)
        self.pm.find_element(AthorizationPageLocators.LOGIN_FIELD).clear()
        self.pm.find_element(AthorizationPageLocators.LOGIN_FIELD).send_keys(email)

        self.pm.locate_element(AthorizationPageLocators.PASSWORD_FIELD)
        self.pm.find_element(AthorizationPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.pm.click_element(AthorizationPageLocators.AUTHORIZATION_BUTTON)
        self.pm.find_element(AthorizationPageLocators.AUTHORIZATION_BUTTON).click()

    def show_error_massage(self):
        self.pm.locate_element(AthorizationPageLocators.ERROR_MESSAGE)
        return self.pm.find_element(AthorizationPageLocators.ERROR_MESSAGE).is_displayed()
