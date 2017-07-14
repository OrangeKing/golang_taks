#!/usr/bin/env python2
"""Python script with selenium test suite for web-app"""

from os import system

from selenium import webdriver


def check_register():
    """Verify proper working of registration form"""
    pass


def check_login():
    """Verify proper working of login form"""
    pass


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
    pass


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        system('exit')

    except EOFError:
        system('exit')
