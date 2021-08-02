from selenium.webdriver.common.by import By

from tests.page.page_manager import PagesManager


class MainPageLocators:
    MAIN_PAGE_PUSH_MASSAGE = (By.ID, 'com.ajaxsystems:id/loading')
    ADD_HUB_BUTTON = (By.ID, 'com.ajaxsystems:id/hubAdd')
    ADD_FIRST_HUB_TEXT = (By.ID, 'com.ajaxsystems:id/addFirstHub')
    MENU_BUTTON = (By.ID, 'com.ajaxsystems:id/menuDrawer')
    CANCEL_BUTTON = (By.ID, 'com.ajaxsystems:id/cancel_button')


class MainPage(object):

    def __init__(self, driver):
        self.pm = PagesManager(driver)

    def is_main_page_opened(self):
        self.pm.locate_element(MainPageLocators.MAIN_PAGE_PUSH_MASSAGE)
        return self.pm.find_element(MainPageLocators.MAIN_PAGE_PUSH_MASSAGE).is_displayed()

    def click_cancel_button(self):
        self.pm.click_element(MainPageLocators.CANCEL_BUTTON)
        self.pm.find_element(MainPageLocators.CANCEL_BUTTON).click()

    def add_hub_button_displayed(self):
        self.pm.locate_element(MainPageLocators.ADD_HUB_BUTTON)
        return self.pm.find_element(MainPageLocators.ADD_HUB_BUTTON).is_displayed()

    def add_first_hub_text_displayed(self):
        self.pm.locate_element(MainPageLocators.ADD_FIRST_HUB_TEXT)
        return self.pm.find_element(MainPageLocators.ADD_FIRST_HUB_TEXT).is_displayed()

    def menu_button_displayed(self):
        self.pm.locate_element(MainPageLocators.MENU_BUTTON)
        return self.pm.find_element(MainPageLocators.MENU_BUTTON).is_displayed()
