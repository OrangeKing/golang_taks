from page_objects.landing_page import LandingPage


class LoginPage(LandingPage):
    URI = LandingPage.URI
    def __init__(self, driver):
        self.fields = "form[action='/login/'] > input[name='{}']"
        self.submit = "form[action='/login/'] > input[type=submit]"
        super(LoginPage, self).__init__(driver)


    def fill_field(self, text, name):
        field = self.driver.find_element_by_css_selector(self.fields.format(name))
        self.element_waiter(field).send_keys(text)


    def press_submit(self):
        submit = self.driver.find_element_by_css_selector(self.submit)
        self.element_waiter(submit).click()
