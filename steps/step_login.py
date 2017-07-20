from behave import given, when, then
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


@when("I put '{text}' into '{name}' field on login form")
def fill_login_form(context, text, name):
    login_page = LoginPage(context.driver)
    login_page.fill_field(text, name)


@when("I press submit button on login form")
def submit_login_form(context):
    login_page = LoginPage(context.driver)
    login_page.press_submit()


@then("I should be logged in")
def user_logged(context):
    home_page = HomePage(context.driver)
    home_page.driver.refresh()
    assert home_page.session_exist()
    assert home_page.is_current_page()
