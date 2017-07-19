from behave import given, when, then
from page_objects import database

@given(u"there are no users")
def db_clear(context):
    database.remove_all_users()


@given(u"there is a user named '{username}' with password '{password}' and email '{email}'")
def create_user(context, username, password, email):
    database.create_user(username, password, email)
    database.user_exist(username)


@then(u"there should be user named '{username}' with password '{password}' and email '{email}'")
def create_user(context, username, password, email):
    database.create_user(username, password, email)
    database.user_exist(username)


@then(u"there should be no user named '{username}'")
def lookup_user(context, username):
    assert not database.user_exist(username)
