from page_objects.task_form import TaskForm
from selenium.webdriver.support.ui import Select


class EditForm(TaskForm):
    URI = TaskForm.URI
    def __init__(self, driver):
        super(EditForm, self).__init__(driver)
        self.driver = driver
        self.add_button = "a[role='menuitem'] > span[class*='glyphicon-pencil']"
        self.priority = "form[action='/update/'] input[name='priority']"
        self.submit = "div[class='modal-footer'] > input[type='submit']"

        self.options = "a[role='menuitem'] > span[class*='glyphicon-{}']"


    def click_option(self, name):
        option = self.driver.find_element_by_css_selector(self.options.format(name))
        self.element_waiter(option).click()
