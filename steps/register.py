from behave import given, when, then


@when("I will see registration form")
def show_signup_form(context):
    assert context.failed is False


@when("I put {text} into {name} field on sign up form")
def fill_signup_form(context, text, name):
    assert context.failed is False


@when("I press submit button on sign up form")
def submit_signup_form(context):
    assert context.failed is False
