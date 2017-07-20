from behave import given, when, then
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.landing_page import LandingPage


@given("I am logged as '{username}' with password '{password}'")
def log_user(context, username, password):
    LandingPage(context.driver).open()
    login_page = LoginPage(context.driver)
    login_page.fill_field(username, "username")
    login_page.fill_field(password, "password")
    login_page.press_submit()


@when("I click the logout button")
def click_logout(context):
    home_page = HomePage(context.driver)
    home_page.press_logout()


@then("I should be logged out")
def user_logged_out(context):
    landing_page = LandingPage(context.driver)
    assert landing_page.is_current_page()
