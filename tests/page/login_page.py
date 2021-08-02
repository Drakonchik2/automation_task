from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTHORIZATION_BUTTON = (By.ID, 'com.ajaxsystems:id/login')


class LoginPage(object):

    def __init__(self, driver):

        self.driver = driver

    def open_authorization_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.AUTHORIZATION_BUTTON))
        self.driver.find_element(*LoginPageLocators.AUTHORIZATION_BUTTON).click()





