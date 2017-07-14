#!/usr/bin/env python2
"""Python script with selenium test suite for web-app"""

from os import system

from selenium import webdriver


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


def check_add_category():
    """Verify proper working of adding categories"""
    pass


def check_add_task():
    """Verify proper working of adding tasks"""
    pass


def check_edit_task():
    """Verify proper working of editing task priority"""
    pass


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


def check_logout():
    """Verify proper working of logout task"""
    pass


def main():
    """main script"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081")

    test_string = "bambo"
    check_register(driver, test_string)
    check_login(driver, test_string)

    raw_input("Press enter key to exit\n")
    driver.quit()

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        system('exit')

    except EOFError:
        system('exit')
