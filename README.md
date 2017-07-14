## Synopsis

A selenium-based python application dedicated for testing toto-list manager web app:
```
https://github.com/thewhitetulip/Tasks
```
## Running the application
*Application runs under Python 2.7.12, for python3 use 2to3 script*
1. **Install prerequisites:**
```bash
pip2 install selenium
```
Apart from selenium framework, chrome webdriver is needed in a $PATH accessible directory:
```
https://sites.google.com/a/chromium.org/chromedriver/downloads
```
2. **Clone/fetch project**
```bash
git clone git@gitlab.mobica.com:int_noka/selenium_tutorial.git
```
3. **Run:**
```bash
 $ ./test.py
```

## Excercise
A program that functions as a test suite for **To-do list app**. <br>
It allows to verify following functionalities:
* REGISTER new user
* LOG as newly registered user
* ADD 2 new CATEGORIES
* ADD 3 TASKS to each of created categories
* EDIT a task, changing its PRIORITY
* for one category, MARK every task as DONE
* for the other, REMOVE every task
* CHECK if there is no TO-DO TASKS
* CHECK for right amount of DONE tasks
* CHECK for right amount of REMOVED tasks
* LOGOUT
