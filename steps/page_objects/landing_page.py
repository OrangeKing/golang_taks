from page_objects.base_page import BasePage

class LandingPage(BasePage):
    URI = 'http://localhost:8081/login'
    def __init__(self, driver):
        super(LandingPage, self).__init__(driver)
