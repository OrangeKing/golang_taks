from behave import given, when, then
from page_objects.home_page import HomePage


@when(u"I click the menu button")
def click_menu(context):
    home_page = HomePage(context.driver)
    home_page.press_menu()


@when(u"I put '{text}' into name field on category form")
def fill_category(context, text):
    home_page = HomePage(context.driver)
    home_page.fill_category(text)


@when(u"I press submit button on category form")
def press_submit(context):
    home_page = HomePage(context.driver)
    home_page.press_submit()
