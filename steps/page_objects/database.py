import sqlite3

DB_PATH = '/home/int_noka/Desktop/python/selenium_tutorial/App/tasks.db'


def remove_all_users():
    db_conn = sqlite3.connect(DB_PATH)
    db_conn.execute("DELETE from user")
    db_conn.commit()


def remove_all_categories():
    db_conn = sqlite3.connect(DB_PATH)
    db_conn.execute("DELETE from category")
    db_conn.commit()

def remove_all_tasks():
    db_conn = sqlite3.connect(DB_PATH)
    db_conn.execute("DELETE from task")
    db_conn.commit()


def user_exist(name, password=None, email=None):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from user WHERE username="{}"'.format(name)

    if password:
        query += ' AND password="{}"'.format(password)
    if email:
        query += ' AND email="{}"'.format(email)

    cursor = conn.execute(query)
    result = cursor.fetchall()

    if len(result) != 1:
        print('Number of users with name {}: {}'.format(name, len(result)))
        return False
    _, name_db, password_db, email_db = result[0]

    if not password:
        password_db = None
    if not email:
        password_db = None
    return (name_db == name and password_db == password and email_db == email)


def category_exist(name):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from category WHERE name="{}"'.format(name)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    _, name_db, _ = result[0]
    return (name_db == name)


def no_category_exist():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * from category"

    cursor = conn.execute(query)
    result = cursor.fetchall()

    if result != 0:
        print('Number of categories: {}'.format(len(result)))
        return False
    return True


def no_task_exist():
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from task'
    cursor = conn.execute(query)
    result = cursor.fetchall()

    if result != 0:
        print('Number of tasks: {}'.format(len(result)))
        return False
    return True


def task_exist(name, user):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from task WHERE title="{}" AND user_id={}'.format(name, get_user_id(user))
    cursor = conn.execute(query)
    result = cursor.fetchall()
    name_db = result[0][1]
    return (name_db == name)


def task_completed(taskname, username):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from task WHERE title="{}" AND user_id={} AND task_status_id={}'.format(taskname, get_user_id(username), 1)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    name_db = result[0][1]
    return (name_db == taskname)


def task_deleted(taskname, username):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from task WHERE title="{}" AND user_id={} AND task_status_id={}'.format(taskname, get_user_id(username), 3)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    name_db = result[0][1]
    return (name_db == taskname)


def verify_priority(name, user, priority):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT * from task WHERE title="{}" AND user_id={} AND priority={}'.format(name, get_user_id(user), get_priority_value(priority))
    cursor = conn.execute(query)
    result = cursor.fetchall()
    name_db = result[0][1]
    return (name_db == name)


def create_user(name, password, email):
    db_conn = sqlite3.connect(DB_PATH)
    db_conn.execute("INSERT INTO user (username, password, email) VALUES('{}', '{}', '{}')".format(name, password, email))
    db_conn.commit()


def get_user_id(name):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT id from user WHERE username="{}"'.format(name)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    if len(result) != 1:
        return False
    result = result[0][0]
    return result


def get_category_id(name, user_id):
    conn = sqlite3.connect(DB_PATH)
    query = 'SELECT id from category WHERE name="{}" AND user_id={}'.format(name, user_id)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    result = result[0][0]
    return result


def get_priority_value(priority):
    if priority == "High":
        i = 3
    elif priority == "Medium":
        i = 2
    elif priority == "Low":
        i = 1
    else:
        print("No such priority to be selected")
        return False
    return i


def create_category(name, username):
    db_conn = sqlite3.connect(DB_PATH)
    db_conn.execute("INSERT INTO category (name, user_id) VALUES('{}', {})".format(name, get_user_id(username)))
    db_conn.commit()


def create_task(taskname, username, task_category, task_priority):
    db_conn = sqlite3.connect(DB_PATH)
    time = '2001-07-03 13:33:37'
    db_conn.execute("INSERT INTO task (title, content, task_status_id, created_date, priority, cat_id, user_id, hide) VALUES('{}', '{}', {}, '{}', '{}', {}, {}, {})".format(
        taskname, '', 2, time, get_priority_value(task_priority), get_category_id(task_category, get_user_id(username)), get_user_id(username), 0))
    db_conn.commit()
