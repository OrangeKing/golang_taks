#!/usr/bin/env python2
"""Python script with selenium test suite for web-app
      implement action chains TODO
      implement cli verification TODO
      implement docker container auto building TODO
      implement random strings TODO
      implement user input TODO
      implement page context conditions TODO """

import time
from os import system

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import Select


def check_register(driver, test_string):
    """Verify proper working of registration form"""
    uname = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                "input[name='username']")
    upasswd = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                  "input[name='password']")
    uemail = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                 "input[name='email']")
    usubmit = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                  "input[type='submit']")

    uname.send_keys(test_string)
    upasswd.send_keys(test_string)
    uemail.send_keys(test_string + "@demo.com")
    usubmit.click()


def check_login(driver, test_string):
    """Verify proper working of login form"""
    uname = driver.find_element_by_css_selector("form[action='/login/'] >"
                                                "input[name='username']")
    upasswd = driver.find_element_by_css_selector("form[action='/login/'] >"
                                                  "input[name='password']")
    usubmit = driver.find_element_by_css_selector("form[action='/login/'] >"
                                                  "input[type='submit']")

    uname.send_keys(test_string)
    upasswd.send_keys(test_string)
    usubmit.click()


def check_add_category(driver, test_string):
    """Verify proper working of adding categories"""
    # action = action_chains.ActionChains(driver) TODO
    sidebar = driver.find_element_by_css_selector(
        "span[class*='glyphicon-align']")
    # if sidebar.parent._web_element_cls.get_attribute(class) == TODO
    # ("sidebar-toggle sidebar-toggle-opened"):
    cname = driver.find_element_by_css_selector(
        "form[action='/add-category/'] > span > input[name='category']")
    csubmit = driver.find_element_by_css_selector(
        "form[action='/add-category/'] > span > input[type='submit']")

    sidebar.click(); time.sleep(1)
    cname.send_keys(test_string); time.sleep(1)
    csubmit.click(); time.sleep(1)


def check_add_task(driver, taskname, category):
    """Verify proper working of adding tasks"""
    add_btn = driver.find_element_by_css_selector(
        "button[class*='btn-danger btn glyphicon glyphicon-plus']")
    add_title = driver.find_element_by_css_selector(
        "form[action='/add/'] input[name='title']")
    add_priority = driver.find_elements_by_css_selector(
        "form[action='/add/'] input[name='priority']")
    add_category = Select(driver.find_element_by_css_selector(
        "form[action='/add/'] select[name='category']"))
    add_submit = driver.find_element_by_css_selector("input[id='addNoteBtn']")

    add_btn.click()
    time.sleep(1)
    add_title.send_keys(taskname)
    time.sleep(1)
    add_priority[1].click()  # mocked, for a time being TODO
    time.sleep(1)
    add_category.select_by_value(category)  # not validated TODO
    time.sleep(1)
    add_submit.click()


def check_edit_task(driver, taskname):
    """Verify proper working of editing task priority"""
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        header = task.find_element_by_css_selector("p[class*='noteHeading']")
        if str(header.text) == taskname:
            edit_btn = task.find_element_by_css_selector(
                "a[role='menuitem'] > span[class*='glyphicon-pencil']")
            edit_btn.click()
            time.sleep(1)

            edit_priority = driver.find_elements_by_css_selector(
                "form[action='/update/'] input[name='priority']")
            edit_submit = driver.find_element_by_css_selector(
                "div[class='modal-footer'] > input[type='submit']")

            edit_priority[0].click()  # value mocked TODO
            time.sleep(1)
            edit_submit.click()
            time.sleep(1)


def check_mark_done():
    """Verify proper working of marking task as done"""
    pass


def check_remove_task():
    """Verify proper working of removing task"""
    pass


def checkif_done():
    """Verify if accurate number of tasks are in done state"""
    pass


def checkif_removed():
    """Verify if accurate number of tasks are removed"""
    pass


def checkif_todo():
    """Verify if any number of todo-tasks"""
    pass


def check_logout(driver):
    """Verify proper working of logout task"""
    logout_btn = driver.find_element_by_css_selector(
        "button[data-original-title='Logout']")
    logout_btn.click()


def main():
    """main script"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081")

    test_string = "helloworld"

    #check_register(driver, test_string)
    check_login(driver, test_string)
    #check_add_category(driver, "katA")
    #check_add_category(driver, "katB")
    #check_add_task(driver, "hello", "katA")
    #check_add_task(driver, "welcome", "katB")
    check_edit_task(driver, "welcome")
    check_logout(driver)

    raw_input("Press enter key to exit\n")
    driver.quit()

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        system('exit')

    except EOFError:
        system('exit')
