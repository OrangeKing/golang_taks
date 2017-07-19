from behave import given, when, then
from page_objects.landing_page import LandingPage


@when("I go to landing page")
def goto_landing_page(context):
    LandingPage(context.driver).open()
