from behave import given, when, then
from page_objects import database

@given("there are no users")
def db_clear_users(context):
    database.remove_all_users()


@given("there are no categories")
def db_clear_categories(context):
    database.remove_all_categories()


@given("there is a user named '{username}' with password '{password}' and email '{email}'")
def create_user(context, username, password, email):
    database.create_user(username, password, email)
    database.user_exist(username)


@given("there is a category named '{name}' for user '{username}'")
def step_impl(context, name, username):
    database.create_category(name, username)
    database.category_exist(name)


@then("there should be user named '{username}' with password '{password}' and email '{email}'")
def create_user(context, username, password, email):
    database.create_user(username, password, email)
    database.user_exist(username)


@then("there should be no user named '{username}'")
def lookup_user(context, username):
    assert not database.user_exist(username)


@then("there should be a category named '{name}'")
def lookup_category(context, name):
    database.category_exist(name)


@then("there should be no categories")
def no_categories(context):
    database.no_category_exist()