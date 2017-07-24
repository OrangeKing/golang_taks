from page_objects.base_page import BasePage

class LandingPage(BasePage):
    URI = "{}login/".format(BasePage.URI)

    def __init__(self, driver):
        super(LandingPage, self).__init__(driver)
