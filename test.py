#!/usr/bin/env python2
"""Python script with selenium test suite for web-app"""

import random
from os import system

import docker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

import namesgenerator


def element_waiter(driver, element):
    """Element waiting decorator"""
    return WebDriverWait(driver, 10).until(EC.visibility_of(element))


def check_register(driver, test_string):
    """Verify proper working of registration form"""
    uname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "form[action='/signup/'] >"
                                        "input[name='username']")))

    upasswd = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                  "input[name='password']")
    uemail = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                 "input[name='email']")
    usubmit = driver.find_element_by_css_selector("form[action='/signup/'] >"
                                                  "input[type='submit']")

    element_waiter(driver, uname).send_keys(test_string)
    element_waiter(driver, upasswd).send_keys(test_string)
    element_waiter(driver, uemail).send_keys(test_string + "@demo.com")
    element_waiter(driver, usubmit).click()


def check_login(driver, test_string):
    """Verify proper working of login form"""
    uname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "form[action='/login/'] >"
                                        "input[name='username']")))
    upasswd = driver.find_element_by_css_selector("form[action='/login/'] >"
                                                  "input[name='password']")
    usubmit = driver.find_element_by_css_selector("form[action='/login/'] >"
                                                  "input[type='submit']")

    element_waiter(driver, uname).send_keys(test_string)
    element_waiter(driver, upasswd).send_keys(test_string)
    element_waiter(driver, usubmit).click()


def check_add_category(driver, test_string):
    """Verify proper working of adding categories"""
    sidebar = driver.find_element_by_css_selector(
        "span[class*='glyphicon-align']")
    cname = driver.find_element_by_css_selector(
        "form[action='/add-category/'] > span > input[name='category']")
    csubmit = driver.find_element_by_css_selector(
        "form[action='/add-category/'] > span > input[type='submit']")

    element_waiter(driver, sidebar).click()
    element_waiter(driver, cname).send_keys(test_string)
    element_waiter(driver, csubmit).click()


def check_add_task(driver, taskname, category, priority):
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

    element_waiter(driver, add_btn).click()
    element_waiter(driver, add_title).send_keys(taskname)
    element_waiter(driver, add_priority[priority]).click()
    add_category.select_by_value(category)
    element_waiter(driver, add_submit).click()


def check_edit_task(driver, taskname, priority):
    """Verify proper working of editing task priority"""
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        header = driver.find_element_by_css_selector(
            "div[class='note'] > p[class*='noteHeading']")
        if str(header.text).strip == taskname:
            edit_btn = task.find_element_by_css_selector(
                "a[role='menuitem'] > span[class*='glyphicon-pencil']")
            element_waiter(driver, edit_btn).click()

            edit_priority = driver.find_elements_by_css_selector(
                "form[action='/update/'] input[name='priority']")
            edit_submit = driver.find_element_by_css_selector(
                "div[class='modal-footer'] > input[type='submit']")

            element_waiter(driver, edit_priority[priority]).click()
            element_waiter(driver, edit_submit).click()


def check_mark_done(driver, taskname):
    """Verify proper working of marking task as done"""
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        header = task.find_element_by_css_selector("p[class*='noteHeading']")
        if str(header.text) == taskname:
            edit_btn = task.find_element_by_css_selector(
                "a[role='menuitem'] > span[class*='glyphicon-check']")
            element_waiter(driver, edit_btn).click()
            return


def check_remove_task(driver, taskname):
    """Verify proper working of removing task"""
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        header = task.find_element_by_css_selector("p[class*='noteHeading']")
        if str(header.text) == taskname:
            rm_btn = task.find_element_by_css_selector(
                "a[role='menuitem'] > span[class*='glyphicon-trash']")
            element_waiter(driver, rm_btn).click()
            return


def checkif_done(driver, category, task_number):
    """Verify if accurate number of tasks are in done state"""
    driver.get("http://localhost:8081/completed")
    counter = 0
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        task_cat = task.find_element_by_css_selector("a[href*='category']")
        if str(task_cat.text) == category:
            counter += 1
    if counter == task_number:
        print("Success: correct number of completed for " + str(category))
    else:
        print("Failure: wrong number of tasks for " + str(category))


def checkif_removed(driver, category, task_number):
    """Verify if accurate number of tasks are removed"""
    driver.get("http://localhost:8081/deleted")
    counter = 0
    tasks = driver.find_elements_by_css_selector("div[class='note']")
    for task in tasks:
        task_cat = task.find_element_by_css_selector("a[href*='category']")
        if str(task_cat.text) == category:
            counter += 1
    if counter == task_number:
        print("Success: correct number of removed for " + str(category))
    else:
        print("Failure: wrong number of tasks for " + str(category))


def checkif_todo(driver):
    """Verify if any number of todo-tasks"""
    driver.get("http://localhost:8081/pending")
    tasks = driver.find_elements_by_css_selector("div[class='note']")

    for task in tasks:
        header = task.find_element_by_css_selector("p[class*='noteHeading']")
        if str(header.text) == "No Tasks here":
            print("Test succeed: no tasks pending")
        else:
            print("Test failed: tasks found in to-do section")


def check_logout(driver):
    """Verify proper working of logout task"""
    logout_btn = driver.find_element_by_css_selector(
        "button[data-original-title='Logout']")
    logout_btn.click()


def main():
    """main script"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("http://localhost:8081")

    # Test cases data
    test_string = "testUser"
    task_names = [namesgenerator.get_random_name() for name in range(6)]
    categories = ["cat_A", "cat_B"]

    # Test cases running
    check_register(driver, test_string)
    check_login(driver, test_string)

    # Add user defined categories
    check_add_category(driver, categories[0])
    check_add_category(driver, categories[1])

    # Add tasks with random names
    for name in task_names:
        index = task_names.index(name) % 2
        check_add_task(driver, name, categories[index], random.randint(0, 2))

    # Assign single task with a random priority
    check_edit_task(driver, task_names[0], random.randint(0, 2))

    # Remove / complete tasks, according to a category
    for name in task_names:
        index = task_names.index(name) % 2
        if index == 0:
            check_mark_done(driver, name)
        else:
            check_remove_task(driver, name)

    # Check page status after removal / completion operations
    checkif_done(driver, categories[0], (len(task_names)/2))
    checkif_removed(driver, categories[1], (len(task_names)/2))
    checkif_todo(driver)

    # Logout
    check_logout(driver)

    raw_input("Press enter key to exit\n")
    driver.quit()


if __name__ == "__main__":

    CLIENT = docker.from_env()
    APP_CONTAINER = CLIENT.containers.run(
        "selenium_tutorial:latest", ports={'8081/tcp': 8081}, detach=True,
        name='selenium_app',
        volumes={'/home/int_noka/Desktop/python/selenium_tutorial/App': {'bind': '/go/src/github.com/thewhitetulip/Tasks', 'mode': 'rw'}})
    try:
        main()

    finally:
        APP_CONTAINER.stop()
        APP_CONTAINER.remove()
        system('exit')
