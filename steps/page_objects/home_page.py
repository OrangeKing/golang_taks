from page_objects.landing_page import BasePage


class HomePage(BasePage):
    URI = "http://localhost:8081"
    def __init__(self, driver):
        self.logout_button = "button[data-original-title='Logout']"
        super(HomePage, self).__init__(driver)


    def session_exist(self):
        return (self.driver.get_cookie('session')) is not None


    def press_logout(self):
        logout = self.driver.find_element_by_css_selector(self.logout_button)
        self.element_waiter(logout).click()
