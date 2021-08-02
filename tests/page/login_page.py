from selenium.webdriver.common.by import By
from tests.page.page_manager import PagesManager


class LoginPageLocators:
    AUTHORIZATION_BUTTON = (By.ID, 'com.ajaxsystems:id/login')


class LoginPage(object):

    def __init__(self, driver):
        self.pm = PagesManager(driver)

    def open_authorization_page(self):
        self.pm.locate_element(LoginPageLocators.AUTHORIZATION_BUTTON)
        self.pm.find_element(LoginPageLocators.AUTHORIZATION_BUTTON).click()





