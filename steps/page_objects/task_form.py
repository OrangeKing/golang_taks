from page_objects.home_page import HomePage
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TaskForm(HomePage):
    URI = HomePage.URI
    def __init__(self, driver):
        self.add_button = "button[class*='btn-danger btn glyphicon glyphicon-plus']"
        self.add_title = "form[action='/add/'] input[name='title']"
        self.priority = "input[type='radio'][name='priority'][value='{}']"
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

        if priority == "High":
            i = 3
        elif priority == "Medium":
            i = 2
        elif priority == "Low":
            i = 1
        else:
            print("No such priority to be selected")
            return False

        # workaround for phantomjs
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.priority.format(i))))
        element.click()


    def select_category(self, category):
        add_category = Select(self.driver.find_element_by_css_selector(self.category))
        add_category.select_by_value(category)


    def press_submit(self):
        submit = self.driver.find_element_by_css_selector(self.submit)
        self.element_waiter(submit).click()
