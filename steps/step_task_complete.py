from behave import given, when, then
from page_objects.completed_page import CompletedPage


@when("I go to the completed page")
def goto_landing_page(context):
    CompletedPage(context.driver).open()


@then("I should be at the completed page")
def step_impl(context):
    CompletedPage(context.driver).is_current_page()


@then("there should be a task named {taskname} in completed page")
def verify_deleted_task(context, taskname):
    assert False
