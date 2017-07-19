from behave import given, when, then


@given("There are no users")
def db_clear(context):
    assert context.failed is False


@then("there should be user named {username} with password {password} and email {email}")
def user_create(context, username, password, email):
    assert context.failed is False
