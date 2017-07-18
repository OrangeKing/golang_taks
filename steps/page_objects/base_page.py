class BasePage(object):
    URI = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URI)
