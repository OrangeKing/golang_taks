from page_objects.home_page import HomePage
from selenium.webdriver.support.ui import Select

class TaskForm(HomePage):
    URI = HomePage.URI
    def __init__(self, driver):
        self.add_button = "button[class*='btn-danger btn glyphicon glyphicon-plus']"
        self.add_title = "form[action='/add/'] input[name='title']"
        self.priority = "form[action='/add/'] input[name='priority']"
        self.category = "form[action='/add/'] select[name='category']"
        self.submit = "input[id='addNoteBtn']"
        super(TaskForm, self).__init__(driver)


    def open_form(self):
        form = self.driver.find_element_by_css_selector(self.add_button)
        self.element_waiter(form).click()


    def fill_name(self, text):
        name_field = self.driver.find_element_by_css_selector(self.add_title)
        self.element_waiter(name_field).send_keys(text)


    def select_priority(self, priority):
        radio_btn = self.driver.find_elements_by_css_selector(self.priority)

        if priority == "High":
            i = 0
        elif priority == "Medium":
            i = 1
        elif priority == "Low":
            i = 2
        else:
            print("No such priority to be selected")
            return False

        self.element_waiter(radio_btn[i]).click()


    def select_category(self, category):
        add_category = Select(self.driver.find_element_by_css_selector(self.category))
        add_category.select_by_value(category)


    def press_submit(self):
        submit = self.driver.find_element_by_css_selector(self.submit)
        self.element_waiter(submit).click()
