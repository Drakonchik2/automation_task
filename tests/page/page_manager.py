from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PagesManager(object):

    def __init__(self, driver):
        self.driver = driver

    def create_page(self, class_):
        return class_(
            self.driver
        )

    def reset_app(self):
        self.driver.reset()

    def find_element(self, data):
        return self.driver.find_element(*data)

    def locate_element(self, data):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(data))

    def click_element(self, data):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(data))