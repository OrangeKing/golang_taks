from behave import given, when, then
from page_objects.home_page import HomePage


@when("I click the menu button")
def click_menu(context):
    home_page = HomePage(context.driver)
    home_page.press_menu()


@when("I put '{text}' into name field on category form")
def fill_category(context, text):
    home_page = HomePage(context.driver)
    home_page.fill_category(text)


@when("I press submit button on category form")
def press_submit(context):
    home_page = HomePage(context.driver)
    home_page.press_submit()
