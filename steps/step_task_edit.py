from behave import given, when, then
from page_objects.edit_form import EditForm


@when("I press the modify task button")
def modify_task(context):
    EditForm(context.driver).open_form()


@when("I select '{priority}' from priority field on edit form")
def add_task_priority(context, priority):
    EditForm(context.driver).select_priority(priority)


@when("I press submit button on edit form")
def add_task_submit(context):
    EditForm(context.driver).press_submit()
