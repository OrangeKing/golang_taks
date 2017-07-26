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
            'http://localhost:8081/api/update-category/?oldName={}&newName={}'.format(oldname, newname))


    def delete_category(self, category):
        self.session.post(
            'http://localhost:8081/api/delete-category/?category={}'.format(category))


# http.HandleFunc("/api/update-category/", views.UpdateCategoryFuncAPI)
# http.HandleFunc("/api/delete-category/", views.DeleteCategoryFuncAPI)

# http.HandleFunc("/api/get-task/", views.GetTasksFuncAPI)
# http.HandleFunc("/api/get-deleted-task/", views.GetDeletedTaskFuncAPI)
# http.HandleFunc("/api/add-task/", views.AddTaskFuncAPI)
# http.HandleFunc("/api/update-task/", views.UpdateTaskFuncAPI)
# http.HandleFunc("/api/delete-task/", views.DeleteTaskFuncAPI)

if __name__ == "__main__":
    try:
        # RestfulSession('test', 'test', 'test@test').signup()
        S = RestfulSession('test', 'test', 'test@test')
        S.get_token()
        S.add_category('test_cat')
        S.add_category('test_cat_2')
        S.add_category('test_cat_3')
        S.update_category('test_cat', 'edited_category')
        S.delete_category('test_cat_3')

    finally:
        system('exit')
