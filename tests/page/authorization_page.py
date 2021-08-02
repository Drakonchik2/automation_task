from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AthorizationPageLocators:
    LOGIN_FIELD = (By.ID, 'com.ajaxsystems:id/login')
    PASSWORD_FIELD = (By.ID, 'com.ajaxsystems:id/password')
    AUTHORIZATION_BUTTON = (By.ID, 'com.ajaxsystems:id/next')
    ERROR_MESSAGE = (By.ID, 'com.ajaxsystems:id/snackbar_text')


class AuthorizationPage(object):

    def __init__(self, driver):

        self.driver = driver

    def fill_fields(self, email, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(AthorizationPageLocators.LOGIN_FIELD))
        self.driver.find_element(*AthorizationPageLocators.LOGIN_FIELD).clear()
        self.driver.find_element(*AthorizationPageLocators.LOGIN_FIELD).send_keys(email)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(AthorizationPageLocators.PASSWORD_FIELD))
        self.driver.find_element(*AthorizationPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(AthorizationPageLocators.AUTHORIZATION_BUTTON))
        self.driver.find_element(*AthorizationPageLocators.AUTHORIZATION_BUTTON).click()

    def show_error_massage(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(AthorizationPageLocators.ERROR_MESSAGE))
        return self.driver.find_element(*AthorizationPageLocators.ERROR_MESSAGE).is_displayed()
