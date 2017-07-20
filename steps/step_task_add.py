from behave import given, when, then
from page_objects.task_form import TaskForm


@when("I press the add task button")
def add_task_open(context):
    TaskForm(context.driver).open_form()


@when("I put '{taskname}' into title field on task form")
def add_task_name(context, taskname):
    TaskForm(context.driver).fill_name(taskname)


@when("I select '{priority}' from priority field on task form")
def add_task_priority(context, priority):
    TaskForm(context.driver).select_priority(priority)


@when("I select '{category}' from category list on task form")
def add_task_category(context, category):
    TaskForm(context.driver).select_category(category)


@when("I press submit button on task form")
def add_task_submit(context):
    TaskForm(context.driver).press_submit()
