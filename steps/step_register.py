from behave import given, when, then
from page_objects.register_page import RegisterPage


@when("I put '{text}' into '{name}' field on sign up form")
def fill_signup_form(context, text, name):
    register_page = RegisterPage(context.driver)
    register_page.fill_field(text, name)


@when("I press submit button on sign up form")
def submit_signup_form(context):
    register_page = RegisterPage(context.driver)
    register_page.press_submit()
