#!/usr/bin/env python2
from os import system

import requests


class RestfulSession(object):
    def __init__(self, uname, passwd, email): #test, test, test@test
        self.uname = uname
        self.passwd = passwd
        self.email = email
        self.session = requests.Session()


    def signup(self):
        requests.post(
            'http://localhost:8081/signup/?username={}&password={}&email={}'.format(
                self.uname, self.passwd, self.email))


    def get_token(self):
        token = requests.post('http://localhost:8081/api/get-token/?username=test&password=test').content
        self.session.headers.update({'Token': token})


    def get_category(self):
        categories = self.session.get('http://localhost:8081/api/get-category/')
        return categories.json()


    def add_category(self, category):
        self.session.post(
            'http://localhost:8081/api/add-category/?category={}'.format(category))


    def update_category(self, oldname, newname):
        self.session.post(
            'http://localhost:8081/api/update-category/{}/?catname={}'.format(oldname, newname))


    def delete_category(self, category):
        self.session.get(
            'http://localhost:8081/api/delete-category/{}/'.format(category))


    def get_task(self):
        tasks = self.session.get('http://localhost:8081/api/get-task/')
        return tasks.json()


    def add_task(self, category, title, content, priority):
        self.session.post(
            'http://localhost:8081/api/add-task/?category={}&title={}&content={}&priority={}'.format(category, title, content, priority))


    def update_task(self, task_id, category, title, content, priority):
        self.session.post(
            'http://localhost:8081/api/update-task/?id={}&category={}&title={}&content={}&priority={}'.format(task_id, category, title, content, priority))


    def delete_task(self, task_id):
        self.session.get(
            'http://localhost:8081/api/delete-task/{}'.format(task_id))


if __name__ == "__main__":
    try:
        RestfulSession('test', 'test', 'test@test').signup()
        S = RestfulSession('test', 'test', 'test@test')
        S.get_token()
        S.add_category('test_cat')
        S.add_category('test_cat_2')
        S.add_category('test_cat_3')
        S.update_category('test_cat', 'edited_category')
        S.delete_category('test_cat_3')

        S.add_task('test_cat_2', 'testtask', ' ', 1)
        S.add_task('test_cat_2', 'secondtask', 'test-content', 3)
        S.update_task(1, 'test_cat_2', 'testtask', 'test-content', 3)
        S.delete_task(2)

    finally:
        system('exit')
