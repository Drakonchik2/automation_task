from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_PUSH_MASSAGE = (By.ID, 'com.ajaxsystems:id/loading')
    ADD_HUB_BUTTON = (By.ID, 'com.ajaxsystems:id/hubAdd')
    ADD_FIRST_HUB_TEXT = (By.ID, 'com.ajaxsystems:id/addFirstHub')
    MENU_BUTTON = (By.ID, 'com.ajaxsystems:id/menuDrawer')
    CANCEL_BUTTON = (By.ID, 'com.ajaxsystems:id/cancel_button')

class MainPage(object):

    def __init__(self, driver):

        self.driver = driver

    def is_main_page_opened(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.MAIN_PAGE_PUSH_MASSAGE))
        return self.driver.find_element(*MainPageLocators.MAIN_PAGE_PUSH_MASSAGE).is_displayed()

    def click_cancel_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainPageLocators.CANCEL_BUTTON))
        self.driver.find_element(*MainPageLocators.CANCEL_BUTTON).click()

    def add_hub_button_displayed(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.ADD_HUB_BUTTON))
        return self.driver.find_element(*MainPageLocators.ADD_HUB_BUTTON).is_displayed()

    def add_first_hub_text_displayed(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.ADD_FIRST_HUB_TEXT))
        return self.driver.find_element(*MainPageLocators.ADD_FIRST_HUB_TEXT).is_displayed()

    def menu_button_displayed(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.MENU_BUTTON))
        return self.driver.find_element(*MainPageLocators.MENU_BUTTON).is_displayed()