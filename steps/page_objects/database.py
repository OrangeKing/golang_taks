import sqlite3

DB_PATH = '/home/int_noka/Desktop/python/selenium_tutorial/App/tasks.db'

def remove_all_users():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('DELETE from user')
    conn.commit()

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
    return (name_db == name and
            password_db == password and
            email_db == email)

def create_user(name, password, email):
    conn = sqlite3.connect(DB_PATH)
    conn.execute('INSERT INTO user (username, password, email) VALUES("{}", "{}", "{}")'.format(name, password, email))
    conn.commit()
