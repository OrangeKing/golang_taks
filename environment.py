"""Definition of pre and post-test behaviors; environment configurations"""
from selenium import webdriver
import docker


def before_all(context):
    """Pre-test behaviors"""
    # CLIENT = docker.APIClient()
    # APP_IMAGE = CLIENT.build(path=".", tag="selenium_tutorial:latest", rm=True)

    # context.client = docker.from_env()
    # context.app_container = context.client.containers.run(
    #     "selenium_tutorial:latest", ports={'8081/tcp': 8081}, detach=True,
    #     name='selenium_app',
    #     volumes={
    #         '/home/int_noka/Desktop/python/selenium_tutorial/App':
    #         {'bind': '/go/src/github.com/thewhitetulip/Tasks', 'mode': 'rw'}})
    # context.driver = webdriver.Chrome()


def after_all(context):
    """Post-test behaviors"""
    context.driver.close()
    # context.app_container.stop()
    # context.app_container.remove()
