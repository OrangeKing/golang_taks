from page_objects.task_form import TaskForm
from selenium.webdriver.support.ui import Select


class EditForm(TaskForm):
    URI = TaskForm.URI
    def __init__(self, driver):
        self.edit_button = "a[role='menuitem'] > span[class='glyphicon glyphicon-pencil']"
        self.edit_priority = "form[action='/update/'] input[name='priority']"
        self.edit_submit = "div[class='modal-footer'] > input[type='submit']"
        super(EditForm, self).__init__(driver)


    def open_form(self):
        form = self.driver.find_element_by_css_selector(self.edit_button)
        self.element_waiter(form).click()


    def select_priority(self, priority):
        radio_btn = self.driver.find_elements_by_css_selector(self.edit_priority)

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


    def press_submit(self):
        submit = self.driver.find_element_by_css_selector(self.edit_submit)
        self.element_waiter(submit).click()
