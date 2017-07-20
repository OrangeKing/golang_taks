from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    URI = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URI)


    def element_waiter(self, element):
        """Element waiting decorator"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of(element))


    def is_current_page(self):
        return self.driver.current_url == self.URI
