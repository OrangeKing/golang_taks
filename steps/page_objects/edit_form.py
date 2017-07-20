from page_objects.task_form import TaskForm
from selenium.webdriver.support.ui import Select

class EditForm(TaskForm):
    URI = TaskForm.URI
    def __init__(self, driver):
        self.add_title = "form[action='/add/'] input[name='title']"
        self.priority = "form[action='/add/'] input[name='priority']"
        self.category = "form[action='/add/'] select[name='category']"
        self.submit = "input[id='addNoteBtn']"
        super(EditForm, self).__init__(driver)
