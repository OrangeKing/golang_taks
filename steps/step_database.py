from behave import given, when, then
from page_objects import database

@given("there are no users")
def db_clear_users(context):
    database.remove_all_users()


@given("there are no categories")
def db_clear_categories(context):
    database.remove_all_categories()


@given("there are no tasks")
def db_clear_tasks(context):
    database.remove_all_tasks()


@given("there is a user named '{username}' with password '{password}' and email '{email}'")
def create_user(context, username, password, email):
    database.create_user(username, password, email)
    database.user_exist(username)


@given("there is a category named '{name}' for user '{username}'")
def create_category(context, name, username):
    database.create_category(name, username)
    database.category_exist(name)


@then("there should be user named '{username}' with password '{password}' and email '{email}'")
def verify_user(context, username, password, email):
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


@then("there should be a task named '{taskname}' for user '{username}'")
def add_task_verify(context, taskname, username):
    database.task_exist(taskname, username)


@then("the '{taskname}' for user '{username}' should have now priority '{priority}'")
def edit_task_verify_priority(context, taskname, username, priority):
    database.verify_priority(taskname, username, priority)


@given("there is a task named '{taskname}' for user '{username}' in category '{category}' with priority '{priority}'")
def create_task(context, taskname, username, category, priority):
    database.create_task(taskname, username, category, priority)


@then("there should be deleted task '{taskname}' for user '{username}'")
def confirm_task_del(context, taskname, username):
    database.task_deleted(taskname, username)


@then("there should be completed task '{taskname}' for user '{username}'")
def confirm_task_done(context, taskname, username):
    database.task_completed(taskname, username)
