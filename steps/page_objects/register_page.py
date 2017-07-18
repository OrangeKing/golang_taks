from page_objects.landing_page import LandingPage

class RegisterPage(LandingPage):
    URI = LandingPage.URI
    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)
