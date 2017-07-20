from behave import given, when, then
from page_objects.home_page import HomePage

@when(u'I click the menu button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the menu button')

@when(u'I put \'test\' into \'name\' field on category form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I put \'test\' into \'name\' field on category form')

@when(u'I press submit button on category form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press submit button on category form')

@then(u'A new category named \'test\' should be created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A new category named \'test\' should be created')
