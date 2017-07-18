from behave import given, when, then

@given('there are no users')
def clear_db(context):
    pass

@then('I will see registration form')
def display_reg_form(context):
    assert context.failed is False
