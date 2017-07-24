from page_objects.base_page import BasePage


class HomePage(BasePage):
    URI = BasePage.URI
    def __init__(self, driver):
        self.logout_button = "button[data-original-title='Logout']"
        self.menu_button = "span[class*='glyphicon-align']"
        self.category_name = "form[action='/add-category/'] > span > input[name='category']"
        self.category_submit = "form[action='/add-category/'] > span > input[type='submit']"
        super(HomePage, self).__init__(driver)


    def session_exist(self):
        return (self.driver.get_cookie('session')) is not None


    def press_logout(self):
        logout = self.driver.find_element_by_css_selector(self.logout_button)
        self.element_waiter(logout).click()


    def press_menu(self):
        menu = self.driver.find_element_by_css_selector(self.menu_button)
        self.element_waiter(menu).click()


    def fill_category(self, text):
        field = self.driver.find_element_by_css_selector(self.category_name)
        self.element_waiter(field).send_keys(text)


    def press_submit(self):
        submit = self.driver.find_element_by_css_selector(self.category_submit)
        self.element_waiter(submit).click()
