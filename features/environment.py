from selenium import webdriver

from features.utils import get_screenshot


def before_all(context):
    context.drv = webdriver.Chrome('driver/chromedriver.exe')


def after_scenario(context, scenario):
    get_screenshot(context)


def after_all(context):
    context.drv.quit()
