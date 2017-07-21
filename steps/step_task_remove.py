from behave import given, when, then
from page_objects.deleted_page import DeletedPage


@then("I go to the deleted page")
def goto_deleted_page(context):
    DeletedPage(context.driver).open()


@then("I should be at the deleted page")
def step_impl(context):
    DeletedPage(context.driver).is_current_page()


@then("there should be a task named {taskname} in deleted page")
def verify_deleted_task(context, taskname):
    assert False
