from behave import given, when, then
from page_objects.landing_page import LandingPage


@when(u"I go to the landing page")
def goto_landing_page(context):
    LandingPage(context.driver).open()


@then(u'I should be at the landing page')
def step_impl(context):
    LandingPage(context.driver).is_current_page()
