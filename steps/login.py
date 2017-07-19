from behave import given, when, then
from page_objects.login_page import LoginPage


@when(u"I put '{text}' into '{name}' field on login form")
def fill_login_form(context, text, name):
    login_page = LoginPage(context.driver)
    login_page.fill_field(text, name)


@when(u"I press submit button on login form")
def submit_login_form(context):
    login_page = LoginPage(context.driver)
    login_page.press_submit()


@then(u'I should be logged in')
def user_logged(context):
    login_page = LoginPage(context.driver)
    assert not(login_page.session_exist() and login_page.is_current_page())
